# 🥗 Daily Diet API

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-DB-%2307405e?logo=sqlite)](https://www.sqlite.org/index.html)
[![Docker](https://img.shields.io/badge/Docker-Ready-%230db7ed?logo=docker)](https://www.docker.com/)
[![Postman Tested](https://img.shields.io/badge/Postman-Tested-orange?logo=postman)](https://www.postman.com/)

A RESTful API built with Flask to manage daily meal tracking — including calories, meal descriptions, and whether each meal is within a diet.  
This project was developed as a learning experience focused on **backend engineering**, **database handling**, **error management**, and **Dockerization**, showcasing skills for a **Junior Data Engineer** role.

---

## 🚀 Features

- ✅ Full CRUD operations for meals
- ⏰ Tracks meal date and time
- 🥦 Flags meals inside or outside the diet
- 🔥 Stores calorie data for future analytics
- 💬 Custom error messages (404, 400)
- 🐳 Docker-ready for containerized environments
- 🧪 Tested via Postman and SQLite CLI

---

## 🧠 Technologies Used

- Python 3.10
- Flask + SQLAlchemy
- SQLite (for local storage)
- Docker & Docker Compose
- Postman (for manual API testing)
- VS Code + WSL2

---

## 📂 Endpoints Overview

| Method | Route              | Description                     |
|--------|--------------------|---------------------------------|
| GET    | `/meals`           | List all meals                  |
| GET    | `/meals/<id>`      | Get specific meal by ID         |
| POST   | `/meals`           | Register a new meal             |
| PUT    | `/meals/<id>`      | Update an existing meal         |
| DELETE | `/meals/<id>`      | Remove a meal from the system   |

---

## 📦 JSON Body Examples

### ➕ Create a Meal (`POST /meals`)

```json
{
  "name": "Lunch",
  "description": "Grilled chicken with quinoa",
  "date_time": "2025-04-21T12:30:00",
  "calories": 430,
  "within_diet": true
}
```

### 🔁 Update a Meal (`PUT /meals/1`)

```json
{
  "name": "Late Lunch",
  "calories": 500,
  "within_diet": false
}
```

---

## 🧪 Running the Project

### ▶️ Option 1: Local (venv)

```bash
git clone https://github.com/matheusvazdata/daily-diet-api.git
cd daily-diet-api
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Access via [http://localhost:5000/meals](http://localhost:5000/meals)

---

### 🐳 Option 2: Docker

```bash
docker-compose build
docker-compose up
```

Container runs on [http://localhost:5000](http://localhost:5000)

> 💾 Your database will be stored in `/instance/meals.db`

---

## 🔐 Example `.env`

```env
SQLALCHEMY_DATABASE_URI = sqlite:///instance/meals.db
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Add this line to `.gitignore`:

```gitignore
.env
instance/meals.db
```

---

## 🗂️ Project Structure

```
daily-diet-api/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── database.py
├── instance/
│   └── meals.db (auto-created)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md
```

---

## 🧠 Error Handling

This API uses custom JSON responses for common issues:

| Error Type | Message Example                                 |
|------------|-------------------------------------------------|
| 404        | `{"error": "Not Found", "message": "Meal not found with the given ID!"}` |
| 400        | `{"error": "Bad Request", "message": "Request error. Check the data sent!"}` |

---

## 💡 Future Ideas

- 🧪 Automated tests with `pytest` and `Flask-Testing`
- 📊 Dashboard to visualize diet history
- 🧾 Export reports (PDF/CSV)
- 🔐 JWT Authentication & User accounts
- 🌐 Deploy on Render / Railway / EC2

---

## 👨‍💻 Author

**Matheus Vaz**  
💼 Aspiring Data Engineer • Backend Developer  
🌐 [Portfolio @ DataCamp](https://www.datacamp.com/portfolio/matheusvazdata)  
🐙 [GitHub](https://github.com/matheusvazdata)  
🔗 [LinkedIn](https://www.linkedin.com/in/matheusvazdata/)

---

## 📝 License

This project is licensed under the MIT License.  
Feel free to fork it, build on top of it and give credits! 🚀👨‍💻