from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

projects = [
    {
        "title": "Flask Portfolio",
        "description": "A personal portfolio website built with Python and Flask.",
        "tech": "Python, Flask, HTML, CSS"
    },
    {
        "title": "Automation Script",
        "description": "A Python script to automate file organization.",
        "tech": "Python"
    },
    {
        "title": "CLI Expense Tracker",
        "description": "A command-line app to track daily expenses.",
        "tech": "Python"
    }
]

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/projects")
def projects_page():
    return render_template("projects.html", title="Projects", projects=projects)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        if request.form.get("company"):
            return redirect(url_for("contact"))
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("All fields are required!", "error")
            return redirect(url_for("contact"))

        conn = sqlite3.connect("messages.db", check_same_thread=False)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )

        conn.commit()
        conn.close()
        # SEND EMAIL
        email_msg = EmailMessage()
        email_msg["Subject"] = "New Portfolio Contact Message"
        email_msg["From"] = EMAIL_ADDRESS
        email_msg["To"] = EMAIL_ADDRESS

        email_msg.set_content(f"""
        You received a new message from your portfolio site.

        Name: {name}
        Email: {email}
        Message:
        {message}
        """)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(email_msg)

        flash("Message sent successfully 🚀", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")
@app.route("/admin")
def admin():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    conn = sqlite3.connect("messages.db", check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, email, message, created_at
        FROM messages
        ORDER BY created_at DESC
    """)
    messages = cursor.fetchall()

    conn.close()

    return render_template("admin.html", messages=messages)
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect(url_for("admin"))

        flash("Invalid credentials", "error")
        return redirect(url_for("admin_login"))

    return render_template("admin_login.html")

if __name__ == "__main__":


    app.run(debug=True)
EMAIL_ADDRESS = "rosmindilip@gmail.com"
EMAIL_PASSWORD = "qbfpflzddrfrfnyj"
