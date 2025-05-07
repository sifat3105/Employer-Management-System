# Employer Management System

A RESTful API project built with Django and Django REST Framework, featuring user authentication with JWT and an employer management system. The project is organized into two Django apps: `accounts` (for authentication) and `employers` (for employer data management).

Production API is live at: **[https://api.zoyrobd.com/ endpoint](https://api.zoyrobd.com)**

---

## Features

- User registration, login, logout (with token blacklisting)
- JWT authentication using `djangorestframework-simplejwt`
- Employer CRUD (Create, Read, Update, Delete) operations
- Custom User model using email as username
- Secure API endpoints with permissions
- Separated app structure for better scalability

---

## Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- Simple JWT
- SQLite (default, can be switched to PostgreSQL/MySQL)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sifat3105/Employer-Management-System.git
cd employer-management
```

### 2. Create Virtual Environment & Activate

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
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

### 5. Run Development Server

```bash
python manage.py runserver
```

---

## API Endpoints

**Base URL:** `https://api.zoyrobd.com`

### Auth (Accounts App)

| Method | Endpoint            | Description            |
|--------|---------------------|------------------------|
| POST   | `/api/auth/signup/` | Register new user      |
| POST   | `/api/auth/login/`  | Login and get tokens   |
| POST   | `/api/auth/logout/` | Blacklist refresh token|
| GET    | `/api/auth/profile/`| Get logged-in user info|

### Employers (Employers App)

| Method | Endpoint                | Description              |
|--------|-------------------------|--------------------------|
| GET    | `/api/employers/`       | List user’s employers    |
| POST   | `/api/employers/`       | Create new employer      |
| GET    | `/api/employers/<id>/`  | Retrieve employer detail |
| PUT    | `/api/employers/<id>/`  | Update employer          |
| DELETE | `/api/employers/<id>/`  | Delete employer          |

---

## Notes

- JWT tokens are required for accessing protected routes.
- Use tools like Postman to test the API.
- Include the `Authorization: Bearer <access_token>` header when making authenticated requests.

---

## Folder Structure

```
employer-management-syatem/
├── accounts/            # Handles user registration, login, logout
├── employers/           # Manages employer-related CRUD
├── project_root/ # Project config and settings
├── requirements.txt
└── README.md
```

---

## License

This project is licensed under the MIT License.

---

## Author

- **Sifat Ali** — [GitHub: sifat3105](https://github.com/sifat3105) | [LinkedIn](https://linkedin.com/in/sifat3105)

