# ✅ Django CBV ToDoApp CRUD | اپلیکیشن مدیریت وظایف با ویوهای کلاس‌محور | CBV-ToDoApp in Django

---

## 🌍 Overview | معرفی | Übersicht

This project is a **simple and modular ToDo application** built with Django using Class-Based Views (CBVs). It enables users to create, view, update, and delete tasks via a clean HTML interface — perfect for learning and practicing CRUD patterns in Django.

این پروژه یک اپلیکیشن ساده برای مدیریت وظایف است که با استفاده از ویوهای کلاس‌محور در Django پیاده‌سازی شده. عملیات CRUD برای مدل وظیفه در قالب‌های HTML و مسیرهای Django پیاده‌سازی شده‌اند.

Dieses Projekt ist eine einfache Aufgabenverwaltung in Django mit CBVs. Benutzer können Aufgaben erstellen, anzeigen, bearbeiten und löschen – ideal für Lernzwecke und saubere Implementierung.

---

## 🚀 Features | ویژگی‌ها | Funktionen

- ✅ Create Tasks  
- 📃 View Tasks  
- ✏️ Edit Tasks  
- 🗑️ Delete Tasks  
- ⚙️ Admin Panel  
- 🔐 LoginRequiredMixin (optional protection)

---

## 📦 Requirements

- Python 3.8+
- Django 4.x+
- SQLite (default) – PostgreSQL optional

---

## 🔧 Installation

```bash
git clone https://github.com/shahramsamar/Django_Cbv_ToDoApp_CRUD.git
cd Django_Cbv_ToDoApp_CRUD

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
📍 Access app at http://127.0.0.1:8000/
```
## 📁 Project Structure
|File/Folder	|Description|
|-----|-----|
|todo/models.py|	Task model with title/description|
|todo/views.py	|CBV for CRUD operations|
|todo/forms.py	|Custom Task form|
|todo/templates/	|HTML pages for list & form|
|todo/urls.py	|URL routing for tasks|
|static/	|CSS and frontend files|
|requirements.txt	|Dependency list|
|manage.py	|Django CLI utility|
## 👨‍💻 Usage
Access tasks list on homepage

Create or edit tasks via intuitive forms

Manage tasks via Django admin panel (/admin)

Protect views using LoginRequiredMixin (optional setup)

## 🛠️ Contributing
- Pull requests, feature suggestions, and issue reports are welcome. To contribute:

```bash
git checkout -b new-feature
git commit -m "Add your message"
git push origin new-feature
```
## 📄 License
This project is open-source and available for educational and personal use.
