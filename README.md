
# 📸 Photo Matching System

The **Photo Matching System** is a Python-Flask-based web application designed to help users automatically match uploaded photos based on facial recognition. The system provides a simple UI for uploading photos, detects and compares faces, and stores matched photos. It also includes Google Drive integration for photo backup and retrieval.

---

## 🚀 Features

- 🔍 **Face Detection & Matching** – Compares new photos with previously uploaded ones using facial recognition.
- 🖼️ **Upload Interface** – Upload single or multiple images at once.
- 🧠 **Automatic Classification** – Automatically stores matched faces in a separate folder.
- ☁️ **Google Drive Integration** – Optional support for syncing files using OAuth or service account.
- 📁 **Organized Storage** – Local folders for uploaded and matched photos.
- 💻 **Web Interface** – Built using Flask for easy accessibility and interactivity.

---

## 🛠️ Technologies Used

| Technology                | Purpose                      |
|--------------------------|------------------------------|
| Python 3.7+              | Backend language             |
| Flask                    | Web framework                |
| face_recognition         | Face comparison engine       |
| OpenCV (cv2)             | Image preprocessing (optional)|
| Google Drive API         | Cloud storage (optional)     |
| HTML, CSS                | Frontend UI                  |

---

## 📂 Project Structure

```

Photo-Matching-system/
│
├── app.py                     # Main Flask application
├── drive\_utils.py             # Google Drive helper functions
├── client\_secrets.json        # Google OAuth credentials
├── service\_account.json       # Google Service Account credentials
├── requirements.txt           # Project dependencies
├── README.md                  # This file
│
├── uploaded\_photos/           # Folder for incoming photos
├── matched/                   # Folder for matched faces
├── uploads/                   # (Optional) Temporary uploads
├── **pycache**/               # Python cache files
├── faceenv/                   # Virtual environment (optional)

````

---

## 📦 Installation Instructions

### ✅ Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- (Optional) Virtual environment tool like `venv` or `virtualenv`

---

### 📥 Step-by-Step Setup

1. **Navigate to the Project Folder**

```bash
cd "E:\web development\Photo-Matching-system"
````

2. **Create a Virtual Environment (Recommended)**

```bash
python -m venv faceenv
faceenv\Scripts\activate  # On Windows
```

3. **Install the Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Application**

```bash
python app.py
```

5. **Access the Web Interface**

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🔐 Google Drive Integration (Optional)

The app supports Google Drive upload/download using both OAuth and Service Account credentials.

### 🧾 Setup Steps:

1. Go to [Google Developer Console](https://console.developers.google.com/)
2. Enable **Google Drive API**
3. Create OAuth 2.0 Credentials and download `client_secrets.json`
4. OR create a Service Account and download `service_account.json`
5. Share the target Google Drive folder with the **Service Account Email**
6. Place both `.json` files in the project root directory

➡️ Drive integration logic is handled in `drive_utils.py`.

---

## 📸 Usage Flow

1. User visits the web interface
2. Uploads a new image
3. System compares it with all images in `uploaded_photos/`
4. If a match is found:

   * Saves it in the `matched/` folder
   * Optionally uploads it to Google Drive
5. Displays the match result on screen

---

## 💡 Use Cases

* 🎓 Student attendance system using photos
* 🏢 Employee photo logging/verification
* 🕵️ Detect duplicate faces across datasets
* 🎉 Identify guests at events or functions

---

## 🔧 Example `requirements.txt`

```txt
Flask==2.1.2
face_recognition==1.3.0
opencv-python==4.7.0.72
numpy==1.21.4
Pillow==9.1.0
google-api-python-client==2.39.0
google-auth==2.6.0
google-auth-oauthlib==0.4.6
```

⚠️ Note: `face_recognition` depends on `dlib`. You may need to install CMake and Visual Studio Build Tools (on Windows) for it to compile correctly.

---

## 🤔 Troubleshooting

* ❌ **face\_recognition not installing**:
  ➜ Install [CMake](https://cmake.org/download/) and [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

* ❌ **ModuleNotFoundError**:
  ➜ Make sure you activated the virtual environment and installed all packages.

* ❌ **Google Drive errors**:
  ➜ Ensure the Drive folder is shared with the email found in `service_account.json`.

* ❌ **Port issues / Flask not running**:
  ➜ Check if port `5000` is already in use or if there's a traceback in the terminal.

---

## 📈 Future Improvements

* ✨ Add face bounding box previews
* 🔐 Add user login & auth (JWT or Flask-Login)
* 🗃️ Save match logs in a database (SQLite/MongoDB)
* 🧠 Confidence threshold adjustments for accuracy
* 📤 Drag-and-drop multi-image uploads
* 📊 Analytics dashboard for usage tracking

---

## 👤 Author

**Tejas Padaki**
Founder @ Yukti Yantra
B.Tech Final Year @ Sanjay Ghodawat University
🚀 MERN Stack | Python | AI/ML | Cloud Enthusiast

🔗 [LinkedIn](https://linkedin.com/in/tejas-padaki)
🔗 [Portfolio](https://tejas-p.onrender.com/)
🔗 [GitHub](https://github.com/tejas-padaki)

---

## 📝 License

This project is licensed for **educational and demo purposes**. For commercial use, please contact the author.

