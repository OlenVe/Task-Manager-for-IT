# 🧠 Task Manager for IT Teams

A modern Django application for managing IT projects, tasks, and teams.  
Perfect for small internal teams who want to efficiently plan work, assign tasks, and keep everything under control.

---

## 🚀 Key Features

- 📁 Projects with descriptions, assigned teams, and tasks
- ✅ Tasks with descriptions, deadlines, priority levels, types, and status tracking
- 👥 Teams with role-based member assignment
- 👨‍💻 Custom `Worker` user model with position, team, and project
- 📨 Email confirmation during user registration
- 📊 Admin panel and modern Bootstrap-based interface
- 🔐 Authentication, authorization, and access control
- 🖼️ Intuitive UI with Bootstrap 5 cards, forms, and tables

### 🧪 In Development

- 💬 Task discussions (chat-style comments)

---

## 🛠️ Technologies

- Django 4+
- Python 3.10+
- PostgreSQL (or SQLite for local development)
- Bootstrap 5
- HTML5 + CSS3
- Django Templates
- Soft UI Dashboard Django Template
- Email backend for user activation

---

## 📦 Installation

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/OlenVe/Task-Manager-for-IT.git
cd Task-Manager-for-IT
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the project root directory with the following content (example):

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=Task Manager <noreply@example.com>
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to access the application.

## Testing
Run tests with:
```bash
python manage.py test tasker.tests
```

