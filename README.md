# 🧾 Django To-Do App

A **To-Do List Web Application** built with Django that allows users to **add, view, update, and delete tasks**.

---

## 🚀 Features

- ✅ Add new tasks  
- 📋 Fetch tasks from the database  
- ✏️ Update existing tasks (mark as completed or edit title)  
- ❌ Delete tasks  


---

## 🧠 Learnings

This project helped in understanding and practicing:

- Django’s **Model-View-Template (MVT)** architecture  
- Using **Django ORM** (Object Relational Mapper)  
- Performing **CRUD operations** (Create, Read, Update, Delete)  
- Working with **Django Admin**  
- Setting up **URLs, Views, and Templates**  
- Handling **forms** and **database migrations**  


---

## 🛠️ Technologies Used

- **Python**  
- **Django** 5.1.6  
- **SQLite**  
- **HTML / CSS / Bootstrap**

---


## 🧩 Project Setup

### 1. Clone the Repository
```bash

git clone https://github.com/Bhairab-Nath/Todo-App-Django-Project.git

```

### 2. Create Virtual Environment & Activate
```bash

python -m venv env
source env/Scripts/activate        # For Windows
# or
source env/bin/activate     # For Mac/Linux

```

### 3. Install Dependencies
```bash

pip install -r requirements.txt

```

### 4. Apply Migrations
```bash

python manage.py makemigrations
python manage.py migrate

```

### 5. Create Superuser (for Admin Panel)
```bash

python manage.py createsuperuser

```

### 6.Run Server
```bash

python manage.py runserver

```

### 7. Access the App

🌐 Open: http://127.0.0.1:8000/
🔑 Admin Panel: http://127.0.0.1:8000/admin/