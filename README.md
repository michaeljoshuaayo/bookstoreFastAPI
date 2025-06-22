# 📚 FastAPI Bookstore API

A simple FastAPI project for managing a collection of books.  
This API supports creating, retrieving, updating, and deleting books with SQLite for data storage and Pydantic for data validation.

## 🧾 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) for development server
- [Pytest](https://docs.pytest.org/) for testing

---

## ⚙️ Installation & Setup

### 1. Clone or Download the Repository

```bash
git clone https://github.com/your-username/bookstore-api.git
cd bookstore-api
```

Or if this is already your local project:

```bash
cd path/to/your/bookstore/project
```

---

### 2. Set Up Virtual Environment

```bash
python -m venv venv
```

Activate it:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
uvicorn main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000/docs
```

You’ll see the interactive Swagger UI to test all endpoints.

---

### 5. Run Tests (Optional)

```bash
pytest
```



## 📬 Contact

If you have questions please contact:
- **Author:** Michael Joshua P. Ayo
- **Email:** michaeljoshuaayo214@gmail.com

---

