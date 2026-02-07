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

## 🛠️ Installation & Setup

Follow these steps to get your development environment ready and the application running.

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your machine. You can verify this by running:
```bash
python --version

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

# For Windows (VS Code / PowerShell)
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py
