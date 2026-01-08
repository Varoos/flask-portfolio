Flask Portfolio Web Application

A modern, full-stack personal portfolio web application built with Python & Flask, featuring a contact system backed by SQLite, an admin dashboard, email notifications, and basic security protections.
This project demonstrates real-world backend development concepts and clean frontend integration.

🌟 Project Overview

This portfolio website was designed not just as a static webpage, but as a functional web application that mimics production-level behavior.

Visitors can:

View portfolio sections (Hero, Projects, Contact)

Submit messages via a contact form

The owner (admin) can:

Receive email notifications on new submissions

View all messages in a protected admin dashboard

Manage messages stored persistently in a database

The project follows a clear separation of concerns between frontend, backend, and data storage.

✨ Key Features
🔹 Frontend

Responsive & modern UI

Dark / Light mode toggle

Smooth animations and transitions

Styled navigation bar and sections

🔹 Backend

Flask-based server architecture

Secure form handling with POST requests

Flash messaging for user feedback

Session-based authentication for admin access

🔹 Database

SQLite for persistent data storage

Structured message table with timestamps

Safe parameterized SQL queries

🔹 Admin Panel

Protected admin login

View submitted messages in a clean table

Messages sorted by most recent first

🔹 Email Integration

Automatic email notifications on form submission

Gmail SMTP integration using App Passwords

🔹 Security

Admin route protection

Session management

Honeypot field for basic spam prevention

🔹 Deployment

Production-ready configuration

Deployed using Gunicorn on Render

🛠 Tech Stack
Backend

Python 3

Flask

SQLite

Gunicorn

smtplib (SMTP Email)

Frontend

HTML5

CSS3

JavaScript

Jinja2 Templates

Deployment & Tools

Render

Git & GitHub

VS Code

🗂 Project Structure
flask-portfolio/
│
├── app.py                # Main Flask application
├── wsgi.py               # Production entry point
├── init_db.py            # Database initialization
├── requirements.txt      # Dependencies
├── messages.db           # SQLite database
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── contact.html
│   ├── admin.html
│   └── admin_login.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md

⚙️ Setup & Installation (Local)
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Run application
python app.py


Then open:

http://127.0.0.1:5000

🔐 Admin Access

Admin login route: /admin/login

Protected admin dashboard: /admin

Uses session-based authentication

Admin credentials can be configured inside app.py.

📧 Email Notifications

Emails are sent automatically when a contact form is submitted

Uses Gmail SMTP with App Password authentication

Secure credentials stored in application configuration

🎯 What This Project Demonstrates

Full-stack Flask application design

Backend-driven form handling

Database integration without ORM

Admin authentication & sessions

Email automation

Security best practices (basic)

Real deployment workflow

🚀 Future Improvements

Environment variable management

Admin message deletion & reply

CAPTCHA integration

REST API version

Migration to PostgreSQL

CI/CD pipeline

👤 Author

Rosmin
Full-Stack Developer
Portfolio Project – Flask Web Application

📄 License

This project is open-source and available for educational and portfolio purposes.
