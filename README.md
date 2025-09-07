Absolutely, Phikani — here’s your **regenerated README file**, tailored to your current API setup and book catalog. It’s clean, presentation-ready, and includes full endpoint URLs for easy copy-paste during your Loomy demo.

---

# 📚 Library Management System API

A production-ready REST API for managing library operations including user registration, book catalog management, secure checkouts, and real-time inventory tracking.

---

## 🚀 Features Overview

- 🔐 **Token-Based Authentication**
- 📦 **Real-Time Inventory Management**
- 🧠 **Automated Business Logic (due dates, overdue tracking)**
- 🔒 **Role-Based Access Control**
- 🔍 **Advanced Search & Filtering**
- ✅ **Smart Validation & Error Handling**

---

## ⚙️ Technology Stack

- **Backend:** Django 5.2.4 + Django REST Framework  
- **Database:** SQLite (dev), PostgreSQL/MySQL (prod)  
- **Auth:** Token-based API authentication  
- **Deployment:** Ready for Heroku, PythonAnywhere, DigitalOcean

---

## 📁 Project Structure

```
Library-Management-System-API/
├── library/
│   ├── models.py          # Book, User, Checkout models
│   ├── serializers.py     # API data formatting
│   ├── views.py           # Business logic endpoints
│   └── urls.py            # API routing
├── library_management/    # Django project settings
└── requirements.txt       # Dependencies
```

---

## 📚 Sample Book Catalog

### 1. The Great Gatsby
- **Author:** F. Scott Fitzgerald  
- **ISBN:** 9780743273565  
- **Publisher:** Scribner  
- **Published Date:** 1925-04-10  
- **Genre:** Fiction  
- **Total Copies:** 3  
- **Available Copies:** 3  
- **Description:** A classic American novel about the Jazz Age

### 2. To Kill a Mockingbird
- **Author:** Harper Lee  
- **ISBN:** 9780446310789  
- **Genre:** Fiction  
- **Total Copies:** 2  
- **Available Copies:** 2

---

## 🧪 Demo Endpoints (Copy & Paste Ready)

### 🔐 1. Login
**POST:**  
`http://localhost:8000/api/auth/login/`

### 📚 2. View Available Books
**GET:**  
`http://localhost:8000/api/books/available/`

### 📦 3. Checkout a Book
**POST:**  
`http://localhost:8000/api/books/{book_id}/checkout/`  
> Replace `{book_id}` with actual UUID

### 📅 4. View My Checkouts
**GET:**  
`http://localhost:8000/api/checkouts/my/`

### 🔒 5. Create Book (Admin Only)
**POST:**  
`http://localhost:8000/api/books/`

### 📊 6. View Admin Stats
**GET:**  
`http://localhost:8000/api/stats/`

### 🔍 7. Search by Title
**GET:**  
`http://localhost:8000/api/books/search/?search=gatsby`

### ✅ 8. Filter Available Only
**GET:**  
`http://localhost:8000/api/books/search/?available_only=true`

---

## 🧠 Business Rules

- Users must be authenticated to checkout books  
- Books can only be checked out if copies are available  
- 14-day checkout period with automatic due date  
- Real-time inventory updates on checkout/return  
- Admins can manage books and view system stats

---

## 🧰 Pre-Demo Setup

1. Start server:  
   ```bash
   python manage.py runserver
   ```

2. Open Postman tabs:
   - Login
   - Available Books
   - Checkout Book
   - My Checkouts
   - Search Books

3. Have token ready:  
   `51b0fdb99da59b753d08326e02079f0381c87388`

4. Ensure at least 2 books with different available copies

---

## 🎯 Key Highlights

| Feature                     | What It Does                                      |
|----------------------------|---------------------------------------------------|
| Real-Time Inventory        | Auto-updates available copies on checkout         |
| Automated Business Logic   | Calculates due dates, tracks overdue status       |
| Enterprise Security        | Token auth + role-based access                    |
| Smart Validation           | Prevents double checkout, validates ISBN          |
| Advanced Search & Filter   | Search by title, genre, availability              |

---

Let me know if you want a version with collapsible sections or Markdown formatting for GitHub. You’re ready to impress.
