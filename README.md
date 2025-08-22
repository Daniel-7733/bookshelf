# Bookshelf (Flask)

A tiny Flask web app to list books and practice templates/static files. Great starter for a personal portfolio.

## ✨ Features
- Home page that lists books (title/author/notes)
- Flask templates (`index.html`) + static assets
- Easy to extend (add forms, database, search, etc.)

## 🗂️ Project Structure
```
website/
├─ app.py
├─ templates/
│  └─ index.html
└─ static/
   └─ css/
```

## 🚀 Quick Start

```bash
# 1) Create & activate a virtual environment (Windows PowerShell)
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# 2) Install deps
pip install -r requirements.txt

# 3) Run
python app.py
# Open http://127.0.0.1:5000/
```

If you don’t have a `requirements.txt` yet:
```bash
pip install flask
pip freeze > requirements.txt
```

## 🔧 Tech
- Python 3.10+
- Flask

## 🛣️ Roadmap (ideas)
- Add a form to add new books
- Persist books (SQLite)
- Edit/delete books
- Basic styling (Bootstrap/Tailwind)
- User auth (optional)
