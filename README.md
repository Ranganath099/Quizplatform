# Quizplatform
# Quiz Platform

## 📌 Objective
The **Quiz Platform** is an interactive online system that allows users to create, attempt, and track quiz performances. Examiners can add multiple-choice questions, and users can take quizzes while competing on a leaderboard.



###  Quiz Creation
- Examiners (registered users) can create quizzes.
- Each quiz contains multiple-choice questions.

###  Quiz Attempting
- Users can take quizzes and receive immediate scores.
- Track progress and performance.

###  Leaderboard
- Displays high scores and rankings of top-performing users.

###  User Authentication
- Secure login and registration system for quiz creators.

###  Analytics
- Provides insights into quiz performance and user engagement.

---

##  Steps to Run the Project

### 1️ Clone the Repository
```bash
git clone https://github.com/Ranganath099/Quizplatform.git
cd Quizplatform
```

### 2️ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️ Run Database Migrations
```bash
python manage.py migrate
```

### 5️ Create a Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### 6️ Start the Development Server
```bash
python manage.py runserver
```

The application will be available at **http://127.0.0.1:8000/**

---

## 📂 Project Structure
```
Quizplatform/
│-- quiz_platform/  # Main Django project files
│-- quiz/           # Quiz app with models, views, and templates
│-- templates/      # HTML templates for UI
│-- db.sqlite3      # Database file
│-- manage.py       # Django management script
│-- requirements.txt # Project dependencies
│-- README.md       # Project documentation
```

---

##  Technologies Used
- **Django** - Web framework
- **SQLite** - Database
- **Bootstrap** - UI styling
- **HTML/CSS** - Frontend

---

##  Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

##  License
This project is open-source under the **MIT License**.

---

###  Contact
For questions or collaboration, reach out via GitHub or email.


