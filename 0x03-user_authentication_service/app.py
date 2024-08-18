#!/usr/bin/env python3
"""
    Flask application
"""
from flask import Flask
from flask import jsonify, request
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """
        Returns the initial route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def users():
    """
        A route to register users
    """
    email, paswd = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({f"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
