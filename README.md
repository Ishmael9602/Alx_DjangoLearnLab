# Library Management System API

A comprehensive REST API for managing library operations including user registration, book catalog management, and checkout/return functionality.

## Demo Overview

This API demonstrates core library management features through secure endpoints that handle user authentication, book inventory, and transaction tracking.

## Quick Demo Setup

```bash
# Clone and setup
git clone <repository-url>
cd Library-Management-System-API
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Server runs at: `http://localhost:8000`

## Demo Endpoints

### 1. User Registration
**Endpoint:** `POST http://localhost:8000/api/auth/register/`

**Sample Request Body:**
```json
{
  "username": "libraryuser",
  "email": "user@library.com",
  "password": "securepass123",
  "password_confirm": "securepass123",
  "first_name": "John",
  "last_name": "Doe"
}
```

**Expected Response:**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "libraryuser",
    "email": "user@library.com"
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 2. User Login
**Endpoint:** `POST http://localhost:8000/api/auth/login/`

**Sample Request Body:**
```json
{
  "username": "libraryuser",
  "password": "securepass123"
}
```

**Expected Response:**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "mael_vundla",
    "email": "v7.vundla@gmail.com"
  },
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 3. Create Book (Admin Required)
**Endpoint:** `POST http://localhost:8000/api/books/`
**Headers:** `Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

**Sample Request Body:**
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9780743273565",
  "publisher": "Scribner",
  "published_date": "1925-04-10",
  "genre": "Fiction",
  "total_copies": 3,
  "available_copies": 3,
  "description": "A classic American novel about the Jazz Age"
}
```

### 4. View Available Books
**Endpoint:** `GET http://localhost:8000/api/books/available/`

**Expected Response:**
```json
{
  "count": 1,
  "results": [
    {
      "book_id": "ca54478e-ef19-4cc6-b0e9-57fa365c081b",
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "genre": "Fiction",
      "available_copies": 3,
      "total_copies": 3,
      "is_available": true
    }
  ]
}
```

### 5. Checkout Book
**Endpoint:** `POST http://localhost:8000/api/books/ca54478e-ef19-4cc6-b0e9-57fa365c081b/checkout/`
**Headers:** `Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

**Sample Request Body:**
```json
{
  "notes": "Looking forward to reading this classic!"
}
```

**Expected Response:**
```json
{
  "message": "Book checked out successfully",
  "checkout": {
    "checkout_id": "abc123-def456-ghi789",
    "book_title": "The Great Gatsby",
    "checkout_date": "2024-08-30T14:30:00Z",
    "due_date": "2024-09-13T14:30:00Z",
    "is_returned": false
  }
}
```

### 6. View My Checkouts
**Endpoint:** `GET http://localhost:8000/api/checkouts/my/`
**Headers:** `Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

**Expected Response:**
```json
{
  "count": 1,
  "results": [
    {
      "checkout_id": "abc123-def456-ghi789",
      "book_title": "The Great Gatsby",
      "book_author": "F. Scott Fitzgerald",
      "checkout_date": "2024-08-30T14:30:00Z",
      "due_date": "2024-09-13T14:30:00Z",
      "is_returned": false,
      "is_overdue": false
    }
  ]
}
```

## Key Features Demonstrated

- **User Authentication**: Secure registration and login with token generation
- **Role-Based Access**: Different permissions for users and administrators
- **Inventory Management**: Real-time tracking of book availability
- **Transaction Tracking**: Complete checkout and return workflow
- **Business Logic**: Due dates, late fees, and availability validation
- **Data Validation**: Comprehensive input validation and error handling

## Technology Stack

- **Backend**: Django 5.2.4 + Django REST Framework
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Authentication**: Token-based API authentication
- **Deployment**: Ready for Heroku, PythonAnywhere, DigitalOcean

## Project Architecture

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

## Business Rules

- Users must be authenticated to checkout books
- Books can only be checked out if copies are available
- 14-day checkout period with automatic due date calculation
- Real-time inventory updates on checkout/return operations
- Admin users can manage books and view system statistics

## Demo Flow

1. **Register** → Get user account
2. **Login** → Receive authentication token
3. **View Books** → Browse available inventory
4. **Checkout** → Borrow a book (requires token)
5. **View Checkouts** → See borrowed books and due dates
6. **Return** → Return book and update inventory
