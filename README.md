# 🎬 Late Show API

A RESTful API built with Flask, PostgreSQL, and JWT Authentication to manage guests, episodes, and appearances for a late-night talk show.

---

## 📦 Tech Stack

- Flask & Flask-RESTful
- PostgreSQL
- SQLAlchemy + Alembic Migrations
- Flask-JWT-Extended for authentication
- Flask-Bcrypt for secure password hashing
- Postman for testing

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:mbxisbankai/late-show-api-challenge.git
cd late-show-api/
```

### 2. Create a virtual environment

```bash
pipenv install && pipenv shell
```

### 3. PostgreSQL setup
- Make sure PostgreSQL is installed and running on your machine and run:
```bash
sudo -i -u postgres
psql
```
```psql
CREATE USER <user> WITH PASSWORD <password>;
CREATE DATABASE <database> OWNER <user>;
GRANT ALL PRIVILEGES ON DATABASE <database> TO <user>;
```

### 4. Create a .env file in /server
```env
SECRET_KEY=your_flask_secret_key
JWT_SECRET_KEY=your_jwt_secret
DATABASE_URL=postgresql://youruser:yourpassword@localhost/late_show_db
```

## ▶️ Running the Project

Go to /server and run:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade head
```

Make sure to export the environment variables
```bash
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
export FLASK_ENV=development
```

Seed the database from the root of the project
```bash
python -m server.seed
```

Run the app
```bash
cd server/
flask run
```

## 🔐 Authentication Flow

- Register

### POST /signup
```json
{
  "username": "Roy",
  "password": "testpassword123"
}
```

- Login

### POST /login
```json
{
  "username": "Zoey",
  "password": "testpassword123"
}
```
- Response:
```json
{
  "token": "<JWT_TOKEN>",
  "user": {
    "id": 1,
    "username": "Zoey"
  }
}
```
## Token Usage
For all protected routes, add this header:
![Authorization Header](/server/assets/Screenshot%20from%202025-06-23%2010-24-52.png "Bearer Token")

## 📡 Route List & Sample Usage
| Method | Route            | Description             | Auth Required  |
| ------ | ---------------- | ----------------------- | -------------- |
| POST   | `/signup`        | Register a new user     | ❌             |
| POST   | `/login`         | Login and get JWT token | ❌             |
| POST   | `/logout`        | Blacklist token         | ✅             |
| GET    | `/guests`        | List all guests         | ❌             |
| POST   | `/guests`        | Add a new guest         | ✅             |
| GET    | `/episodes`      | List episodes           | ❌             |
| DELETE | `/episodes/<id>` | Delete episode          | ✅             |
| GET    | `/appearances`   | List appearances        | ❌             |
| POST   | `/appearances`   | Add appearance          | ✅             |

## Postman Usage Guide
1. Open Postman
2. Input a new collection or manually create requests.

### Example Usage
Request
![Example Request](/server/assets/Screenshot%20from%202025-06-23%2010-44-33.png "Example Request")

Response
![Example Response](/server/assets/Pasted%20image.png)


