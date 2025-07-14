import os
import uuid
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace
from sklearn.cluster import DBSCAN
from werkzeug.utils import secure_filename
from s3_utils import (
    upload_fileobj_to_s3,
    list_photographer_images,
    download_image_from_s3,
    generate_presigned_url
)

app = Flask(__name__)
CORS(app)

def get_embedding_from_file(file_obj):
    try:
        embedding_obj = DeepFace.represent(img_path=file_obj, model_name="ArcFace", enforce_detection=True)
        return np.array(embedding_obj[0]["embedding"])
    except Exception as e:
        print(f"Embedding error: {e}")
        return None

@app.route("/upload_folder", methods=["POST"])
def upload_folder():
    s3_folder = request.form.get("s3_folder", "photographer-uploads").strip().replace(" ", "-")
    if 'folder_images' not in request.files:
        return jsonify({"error": "No images uploaded"}), 400

    images = request.files.getlist('folder_images')
    uploaded_files = []

    for img in images:
        full_path = img.filename.replace("\\", "/")
        s3_key = f"{s3_folder}/{full_path}"
        try:
            img.seek(0)
            url = upload_fileobj_to_s3(img, s3_key=s3_key)
            uploaded_files.append({"filename": full_path, "url": url})
        except Exception as e:
            print("Upload failed:", e)

    return jsonify({
        "status": "Uploaded",
        "uploaded_count": len(uploaded_files),
        "uploaded_files": uploaded_files
    })

@app.route("/selfie_sort", methods=["POST"])
def selfie_sort():
    selfie_file = request.files.get("selfie")
    if not selfie_file:
        return jsonify({"error": "Missing selfie"}), 400

    try:
        selfie_file.seek(0)
        input_embedding = get_embedding_from_file(selfie_file)
        if input_embedding is None:
            return jsonify({"error": "No face detected in selfie"}), 400

        embeddings = [input_embedding]
        streams = ["SELFIE"]
        filenames = ["SELFIE"]

        s3_keys = list_photographer_images()
        for key in s3_keys:
            image_stream = download_image_from_s3(key)
            if not image_stream:
                continue
            image_stream.seek(0)
            embedding = get_embedding_from_file(image_stream)
            if embedding is not None:
                embeddings.append(embedding)
                streams.append(image_stream)
                filenames.append(key)

        embeddings = np.array(embeddings)
        dbscan = DBSCAN(eps=0.45, min_samples=2, metric='cosine')
        labels = dbscan.fit_predict(embeddings)
        selfie_cluster = labels[0]

        matches = []
        for i, label in enumerate(labels[1:], start=1):
            if label == selfie_cluster and label != -1:
                streams[i].seek(0)
                matched_key = f"matched-selfies/{uuid.uuid4().hex}_{filenames[i].split('/')[-1]}"
                url = upload_fileobj_to_s3(streams[i], matched_key)
                matches.append({
                    "filename": filenames[i],
                    "cluster": int(label),
                    "url": url
                })

        return jsonify({
            "status": "success",
            "matched_files": matches,
            "total_matches": len(matches),
            "selfie_cluster": int(selfie_cluster)
        })

    except Exception as e:
        print("Selfie Sort error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
