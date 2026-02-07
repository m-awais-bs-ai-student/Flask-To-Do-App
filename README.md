# Flask TODO Application

A professional, lightweight To-Do List web application built with the **Flask** micro-framework. This project demonstrates core web development concepts including CRUD operations, database management with SQLite, and dynamic template rendering.

---

## 🚀 Features

* **Task Management:** Create, view, and update tasks via a clean web interface.
* **Persistent Storage:** Uses a SQLite database located in the `instance/` folder.
* **Template Inheritance:** Utilizes Jinja2 for a modular frontend structure (`base.html`).
* **Static Asset Management:** Organized directory for CSS, JavaScript, and other assets.

---

## 📁 Project Structure

```text
FLASK/
├── instance/           # Database storage (TODO.db)
├── static/             # Assets (CSS, JS, Images)
├── templates/          # HTML files
│   ├── base.html       # Parent layout
│   ├── index.html      # Main dashboard
│   └── update.html     # Task editing page
├── app.py              # Application logic and routing
└── requirements.txt    # Project dependencies

1️⃣ Clone the Repository: Copy and paste this into your terminal to download your project:
git clone https://github.com/m-awais-bs-ai-student/Flask-To-Do-App.git cd Flask-To-Do-App

2️⃣ Environment Setup
Create and activate your virtual environment to keep your global Python clean:
# Create the environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

3️⃣ Install Necessary Packages
Install everything needed to run the app from your requirements.txt:
pip install -r requirements.txt

4️⃣ Run the App
Start your Flask server:
python app.py
