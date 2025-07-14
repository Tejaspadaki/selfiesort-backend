## 📸 Photo Matching Backend (Flask + S3 + DeepFace)

This is a Flask-based backend for a **face recognition photo matching system**. It allows:

* 📤 Uploading a folder of images (e.g., wedding/event photos) directly to **AWS S3**
* 🤳 Uploading a **selfie** to match against the uploaded images using **face embeddings**
* 🧠 Face detection powered by **DeepFace (ArcFace model)**
* 📂 Organized storage in S3 (uploaded folders and matched folders)
* 🔗 All output URLs are S3-generated public/pre-signed links

---

## 🧠 Features

* Upload photos from photographers directly to AWS S3
* Automatically extract embeddings using `DeepFace`
* Cluster using `DBSCAN` (unsupervised clustering)
* Upload matched images to a separate folder (`matched-selfies/`) in S3
* Serve results through a JSON API (ready for frontend integration)

---

## 🛠️ Technologies Used

* `Flask`
* `DeepFace` (ArcFace)
* `DBSCAN` from `sklearn`
* `AWS S3` for file storage
* `Boto3` (AWS SDK for Python)
* `CORS` for frontend API access

---

## 📁 Project Structure

```
📦 backend/
├── app.py                # Main Flask API
├── s3_utils.py           # AWS S3 helper functions
├── requirements.txt      # Dependencies
```

---

## 🚀 Setup Instructions

### 1. 🧱 Clone the Repo

```bash
git clone https://github.com/yourusername/photo-matching-backend.git
cd photo-matching-backend
```

### 2. 🐍 Create a Virtual Environment

```bash
python -m venv faceenv
source faceenv/bin/activate     # On Windows: faceenv\Scripts\activate
```

### 3. 📦 Install Dependencies

Make sure your Python version is 3.9 or 3.10 (avoid 3.11+ due to DeepFace issues).

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> 💡 If you face issues with `tensorflow` or `numpy`, you may need to tweak version numbers. Let me know and I’ll adjust them for your OS/CPU/GPU.

---

## ⚙️ AWS S3 Configuration

### Set these environment variables in your shell or `.env` file:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=ap-south-1         # e.g. Mumbai
export S3_BUCKET_NAME=your-s3-bucket-name
```

If using a `.env`, install `python-dotenv` and load it from `s3_utils.py`.

---

## ▶️ Run the Flask Server

```bash
python app.py
```

API will be available at: `http://localhost:5000/`

---

## 🧪 API Endpoints

### 📤 Upload Photos

```
POST /upload_folder
Form Data:
- s3_folder (optional): string (e.g., "wedding-july2025")
- folder_images: [files[]] (multiple image files)
```

### 🤳 Match a Selfie

```
POST /selfie_sort
Form Data:
- selfie: file (JPEG or PNG)
```

Response:

```json
{
  "status": "success",
  "matched_files": [
    {
      "filename": "wedding-july2025/photo1.jpg",
      "cluster": 1,
      "url": "https://s3.amazonaws.com/yourbucket/matched-selfies/...jpg"
    }
  ],
  "total_matches": 3,
  "selfie_cluster": 1
}
```

---

## 📦 Example Frontend Repo (Optional)

If you're looking for a frontend built in React, refer to:

* `/frontend/SelfieMatcher.js`
* `/frontend/PhotographerUpload.js`

---

## 📄 License

MIT License. Feel free to modify and use commercially or academically.

---

Let me know if you want:

* ✅ Dockerfile support
* ✅ Swagger/OpenAPI documentation
* ✅ Auto-deployment with Render/EC2/Vercel

I'll help you add those too.
