from flask import Flask, request

import brain

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello my name is Frank"


@app.route("/chat", methods=["POST"])
def chat():
    message = request.data.decode("utf-8")
    return brain.respond_to(message)

