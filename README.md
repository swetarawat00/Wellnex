# WellNex – Day 1 ✅

## 🔧 Backend Setup (Django + DRF)
- Initialized Django project: `wellnex`
- Created apps: `users`, `wellnex`
- Installed `djangorestframework`, `djangorestframework-simplejwt`, etc.
- Configured custom `User` model with email-based login
- Enabled JWT authentication
- Created register and login endpoints
- Created superuser for admin panel access

## 🔐 Auth APIs

| Endpoint               | Method | Description         |
|------------------------|--------|---------------------|
| `/api/users/register/`| POST   | User registration   |
| `/api/token/`         | POST   | JWT login           |
| `/api/token/refresh/` | POST   | Token refresh       |

## 🧪 Tested With:
- Thunder Client / Postman
- Access and refresh token workflow

---

✅ Next: Implement Mood Tracker API

📁 Commit:  
`git commit -m "Day 1: Setup Django project with custom user model and JWT auth"`
