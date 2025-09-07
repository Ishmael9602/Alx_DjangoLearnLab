
```markdown
# Django Learning Lab – ALX Tasks  

This repository contains my progress and solutions for the **ALX Django LearnLab** projects.  
It includes multiple Django apps and exercises focused on building a Library Management project, setting up relationships between models, and implementing a custom user model.  

---

## 📂 Project Structure  

```

ALX\_DjangoLearnLab/
│
├── LibraryProject/               # Main Django project
│   ├── LibraryProject/           # Project settings, urls, wsgi
│   ├── relationship\_app/         # App to manage books, authors, relationships
│   └── manage.py
│
├── advanced\_features\_and\_security/ (work in progress / may be rebuilt)
│   ├── accounts/                 # Custom User model
│   ├── LibraryProject/           # Project folder for advanced tasks
│   └── manage.py
│
└── README.md

````

---

## ⚙️ Setup Instructions  

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd ALX_DjangoLearnLab
````

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > If `requirements.txt` is missing, install Django and Pillow manually:

   ```bash
   pip install django pillow
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

---

## 🏗 Features Implemented

### 1. **LibraryProject – relationship\_app**

* Added `Book` and related models.
* Created a view that renders a list of **book titles and authors**.
* Used template `relationship_app/list_books.html` for rendering.
* Configured URLs and views to support book listings.

### 2. **Custom User Model – accounts**

* Extended `AbstractUser` with:

  * `date_of_birth` field
  * `profile_photo` (ImageField, requires Pillow)
* Created a **CustomUserManager** for handling user creation.
* Updated `settings.py` to use:

  ```python
  AUTH_USER_MODEL = 'accounts.CustomUser'
  ```

### 3. **Admin Integration**

* Registered `CustomUser` model in Django Admin.
* Verified login and superuser creation using the new custom model.

---

## 📌 Common Issues & Fixes

* **ImageField Error (Pillow not installed)**
  Install Pillow:

  ```bash
  pip install pillow
  ```

* **Migration conflicts**
  If you see errors like *InconsistentMigrationHistory*:

  ```bash
  rm -rf accounts/migrations relationship_app/migrations db.sqlite3
  python manage.py makemigrations
  python manage.py migrate
  ```

* **Project Cleanup**
  To restart a task from scratch, simply delete the folder:

  ```bash
  rm -rf advanced_features_and_security
  ```

---

## 📚 Learning Outcomes

* Setting up Django projects and apps.
* Managing models and relationships.
* Creating and using a **custom user model**.
* Handling migrations and common Django errors.
* Running a project with templates, views, and static files.

---

## 🚀 Next Steps

* Rebuild the **advanced\_features\_and\_security** task cleanly.
* Add authentication views (login, logout, register).
* Implement user profile pages and permissions.
* Secure routes and enhance functionality with advanced Django features.



```
