# 📚 Bookshelf (Flask)

A small Flask web application to manage a personal bookshelf. Built to practice **Flask, Jinja templates, static assets, and authentication**. Great as a starter project or portfolio demo.  

---

## ✨ Features
- ✅ **User Authentication**
  - Register, Login, Logout (Flask-Login + hashed passwords)  
- ✅ **Book Management**
  - Add new books  
  - Edit book details  
  - Delete books  
  - See all books in a list  
  - Featured random book on homepage  
- ✅ **Templates & Styling**
  - Base layout (`base.html`) with reusable navbar  
  - Auth layout (`auth_base.html`) for clean login/register pages  
  - Custom CSS per page (`add.css`, `edit.css`, etc.)  
- ✅ **Database**
  - SQLite via SQLAlchemy ORM  
  - User ↔ Books relationship (one-to-many)  

---

## 🗂️ Project Structure
```
website/
├─ app.py              # Main Flask app, routes, auth
├─ db.py               # SQLAlchemy instance
├─ models.py           # User and Book models
│
├─ templates/          # HTML templates (Jinja2)
│  ├─ base.html        # Main layout with navbar
│  ├─ auth_base.html   # Minimal layout for login/register
│  ├─ home.html        # Homepage with featured book
│  ├─ all_books.html   # List of all books
│  ├─ add.html         # Add new book form
│  ├─ edit.html        # Edit book form
│  ├─ delete.html      # Delete confirmation
│  ├─ login.html       # Login page
│  └─ register.html    # Register page
│
├─ static/             # Static assets
│  ├─ css/             # Page-specific CSS files
│  │   ├─ main.css
│  │   ├─ auth.css
│  │   ├─ add.css
│  │   ├─ edit.css
│  │   └─ all_books.css
│  └─ images/
│      └─ stack-of-books.png
│
├─ instance/
│  └─ book.db          # SQLite database (auto-created)
│
├─ requirements.txt    # Python dependencies
└─ README.md           # Project docs
```

---

## 🚀 Quick Start

```bash
# 1) Create & activate a virtual environment
python -m venv .venv
. .venv/Scripts/activate   # Windows PowerShell
# or
source .venv/bin/activate  # Mac/Linux

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
python app.py

# Open in your browser:
http://127.0.0.1:5000/home
```

---

## 🔧 Tech Stack
- **Python 3.10+**
- **Flask** (backend framework)
- **Flask-Login** (authentication)
- **SQLAlchemy** (ORM for SQLite)
- **Jinja2** (templating engine)
- **HTML + CSS** (custom styling)

---

## 🛣️ Roadmap (future ideas)
- Add user-specific book collections (each user sees only their books)  
- Add search and filter by author/title  
- Add pagination for large book lists  
- Add cover image upload for each book  
- Switch to PostgreSQL or MySQL in production  
- Add Docker setup for deployment  

---

⚡ This project helped me practice Flask, authentication, and building CRUD apps with a clean structure.
