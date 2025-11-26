

# Library Management System API

A Django REST Framework project for managing books, authors, categories, borrow requests, and purchase orders. This project includes JWT authentication, user roles, and an admin panel.

---

## Features

- User authentication with JWT tokens
- Custom user model with roles (`member`, `librarian`, `admin`)
- CRUD operations for:
  - Books
  - Authors
  - Categories
  - Borrow Requests
  - Purchase Orders
- Borrow request approval system (decreases book quantity when approved)
- Admin panel for managing users and resources
- API documentation with **Swagger** via drf-spectacular
- RESTful API endpoints

---

## Project Structure

```

LibraryManagementSystemAPI/
├── library/                # Book, Author, Category models and views
├── orders/                 # BorrowRequest, PurchaseOrder models and views
├── users/                  # CustomUser model and authentication
├── LibraryManagementSystemAPI/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── .gitignore

````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/LibraryManagementSystemAPI.git
cd LibraryManagementSystemAPI
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

---

## API Endpoints

| Endpoint                             | Method | Description               |
| ------------------------------------ | ------ | ------------------------- |
| `/api/books/`                        | GET    | List all books            |
| `/api/books/`                        | POST   | Create a new book         |
| `/api/authors/`                      | GET    | List all authors          |
| `/api/authors/`                      | POST   | Create a new author       |
| `/api/categories/`                   | GET    | List all categories       |
| `/api/categories/`                   | POST   | Create a new category     |
| `/api/borrow-requests/`              | GET    | List all borrow requests  |
| `/api/borrow-requests/`              | POST   | Create a borrow request   |
| `/api/borrow-requests/<id>/approve/` | POST   | Approve a borrow request  |
| `/api/purchase-orders/`              | GET    | List all purchase orders  |
| `/api/purchase-orders/`              | POST   | Create a purchase order   |
| `/api/token/`                        | POST   | Obtain JWT token          |
| `/api/token/refresh/`                | POST   | Refresh JWT token         |
| `/api/docs/`                         | GET    | Swagger API documentation |

---

## Notes

* All new users are `member` by default. Roles can be changed only by admin.
* Book quantity decreases when a borrow request is approved.
* API requests require JWT authentication.
* Admin panel available at `/admin/` for managing all resources.

---

## Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

> Never push your `.env` file to GitHub. Keep it secret.

---

## Requirements

* Python 3.11+
* Django 5.1+
* Django REST Framework
* drf-spectacular
* djangorestframework-simplejwt

Install all requirements:

```bash
pip install -r requirements.txt
```


