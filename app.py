from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Interview Preparation Platform Backend Running"


@app.route("/questions")
def get_questions():
    questions = [
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Process Unit",
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Processor Utility"
            ],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which language is widely used for Machine Learning?",
            "options": ["Python", "HTML", "CSS", "C"],
            "answer": "Python"
        }
    ]

    return jsonify(questions)


@app.route("/signup", methods=["POST"])
def signup():

    data = request.json
    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username,password) VALUES (?,?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    return {"message": "User created successfully"}


@app.route("/login", methods=["POST"])
def login():

    data = request.json
    username = data["username"]
    password = data["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}


@app.route("/save_score", methods=["POST"])
def save_score():

    data = request.json
    username = data["username"]
    score = data["score"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO scores(username,score) VALUES (?,?)",
        (username, score)
    )

    conn.commit()
    conn.close()

    return {"message": "Score saved successfully"}

@app.route("/ai_questions")
def ai_questions():

    questions = [
        {
            "question": "What is Machine Learning?",
            "options": [
                "A type of hardware",
                "A method of data analysis that learns patterns",
                "A programming language",
                "A database system"
            ],
            "answer": "A method of data analysis that learns patterns"
        },
        {
            "question": "Which library is commonly used for data analysis in Python?",
            "options": ["NumPy", "Pandas", "Flask", "Django"],
            "answer": "Pandas"
        },
        {
            "question": "What does API stand for?",
            "options": [
                "Application Programming Interface",
                "Advanced Programming Input",
                "Applied Program Internet",
                "Application Process Integration"
            ],
            "answer": "Application Programming Interface"
        }
    ]

    return jsonify(questions)
@app.route("/leaderboard")
def leaderboard():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username,score FROM scores ORDER BY score DESC"
    )

    data = cursor.fetchall()

    conn.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)