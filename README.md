# 📇 Contacts Manager

A desktop contact management application built with **Python, PySide6, and SQLite**.

This project explores **Qt's Model/View architecture**, database integration, CRUD operations, and modular Python application design.

## ✨ Features

* ➕ Add contacts
* 🗑️ Delete contacts
* 🧹 Clear all contacts
* 💾 Persistent SQLite storage
* 🔎 Input validation
* 📊 Live database-backed table
* ⚠️ Confirmation & error dialogs

## 🛠️ Tech Stack

* **Python 3**
* **PySide6 / Qt 6**
* **SQLite**
* **QSqlTableModel / QSqlQuery**
* **Qt Signals & Slots**

## 🏗️ Architecture

```text
contacts_app/
├── contacts.py
└── contact_files/
    ├── main.py
    ├── database.py
    ├── model.py
    ├── views.py
    └── __init__.py
```

The application separates **database, model, and UI logic** into independent modules.

## 🚀 Getting Started

### Install

```bash
pip install PySide6
```

### Run

```bash
python contacts.py
```

The SQLite database is created automatically on first launch.

## 🧠 What I Explored

* Building desktop applications with **PySide6**
* Working with **Qt's Model/View framework**
* Integrating SQLite with a GUI application
* Structuring Python applications into reusable modules
* Working with Qt's **Signals & Slots**
* Managing database edit strategies and CRUD operations

## 🔮 Future Ideas

* 🔍 Search & filtering
* ✏️ Edit contacts
* 📤 CSV / vCard export
* 🌙 Dark mode
* 🧪 Automated tests

---

**Built by ARK13** — a hands-on Python project exploring desktop GUI development, SQLite, and Qt architecture.
