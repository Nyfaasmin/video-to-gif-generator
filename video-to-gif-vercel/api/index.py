from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Nyfa! Flask is working on Vercel 🎉"