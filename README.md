# 📞 Phonebook Application (FastAPI + Vue)

## 🚀 Overview

A full-stack Phonebook application where users can:

* Add contacts
* View contacts
* Update contacts
* Delete contacts

**Tech Stack:**

* **Backend:** FastAPI (Python)
* **Frontend:** Vue 3 (Vite)
* **Database:** PostgreSQL
* **API:** RESTful

---

## 🏗️ Project Structure

```
phonebook-backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       └── contacts.py
│
├── tests/
│   └── test_contacts.py
│
├── .env
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI)

### 1. Create Virtual Environment

#### Windows

```
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Install Dependencies

```
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic[email] python-dotenv pytest httpx slowapi
```

---

### 3. Environment Variables

Create a `.env` file in root:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/phonebook_db
```

---

### 4. Run Server

```
uvicorn app.main:app --reload
```

API:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## 🎨 Frontend Setup (Vue)

### 1. Navigate to frontend

```
cd phonebook-frontend
```

### 2. Install dependencies

```
npm install
npm install axios
```

### 3. Run frontend

```
npm run dev
```

Frontend:

```
http://localhost:5173
```

👉 Open this URL in your browser to use the UI.

⚠️ IMPORTANT:

* Backend **must be running** at `http://127.0.0.1:8000`
* Otherwise frontend API calls will fail

---

## 🔗 API Endpoints

| Method | Endpoint       | Description      |
| ------ | -------------- | ---------------- |
| GET    | /contacts      | Get all contacts |
| POST   | /contacts      | Create contact   |
| GET    | /contacts/{id} | Get one contact  |
| PUT    | /contacts/{id} | Update contact   |
| DELETE | /contacts/{id} | Delete contact   |

---

## 🔐 Security Features

* ✅ Environment-based DB configuration (`.env`)
* ✅ CORS enabled for frontend integration
* ✅ Input validation (Pydantic)
* ✅ Unique constraints (phone, email)

---

## ⚡ Rate Limiting

Implemented using **slowapi**:

```
@limiter.limit("5/minute")
```

* Prevents API abuse
* Returns:

```
429 - Rate limit exceeded
```

---

## 🧪 Testing (pytest)

### Run Tests

```
python -m pytest
```

### Test Coverage

* Create contact
* Get all contacts
* Get by ID
* Update contact
* Delete contact

---

## 🧹 Code Quality

* Modular architecture (routers, services, models)
* Global exception handler for consistent API responses
* Clean validation logic using Pydantic
* Logging enabled via `logging.basicConfig`

---

## 🗄️ Database Setup (PostgreSQL)

### 🔹 Option 1: Local PostgreSQL

1. Install PostgreSQL
2. Create DB:

```
CREATE DATABASE phonebook_db;
```

---

### 🔹 Option 2: Docker (Recommended)

```
docker run -d \
  --name phonebook-db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=phonebook_db \
  -p 5432:5432 \
  postgres
```

---

### 🔹 Verify Connection

* PostgreSQL running on port **5432**
* Credentials match `.env`
* Database exists

---

## 🧱 Database Schema

| Column       | Type      | Description      |
| ------------ | --------- | ---------------- |
| id           | Integer   | Primary Key      |
| name         | String    | Contact name     |
| phone_number | String    | Unique           |
| email        | String    | Optional, Unique |
| address      | Text      | Optional         |
| created_at   | Timestamp | Auto-generated   |

---

## 🧠 Validation Rules

* Name → letters only
* Phone → 10–15 digits (optional +)
* Email → optional but must be valid

---

## 📊 Features

* CRUD operations
* Input validation (frontend + backend)
* Unique constraints
* Pagination support
* Search functionality
* Rate limiting
* API testing with pytest

---

## ⚠️ Notes

* Email is optional but must be valid
* Phone number must be unique
* Backend uses SQLAlchemy ORM

---

## 🚀 Future Improvements

* Docker Compose (full stack)
* CI/CD pipeline
* JWT Authentication
* Role-based access
* Advanced logging (JSON/file-based)

---

## 💯 Status

| Feature       | Status |
| ------------- | ------ |
| Backend API   | ✅      |
| Frontend UI   | ✅      |
| Database      | ✅      |
| Validation    | ✅      |
| Testing       | ✅      |
| Rate Limiting | ✅      |
| Security      | ✅      |

---
