from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# For Vercel's serverless function handler
def handler(environ, start_response):
    return app(environ, start_response)
