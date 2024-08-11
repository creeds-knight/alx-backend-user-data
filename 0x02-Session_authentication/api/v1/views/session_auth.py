#!/usr/bin/env python3
"""
    A file to handle session based views
"""
import os
from api.v1.views import app_views
from flask import request, abort, jsonify
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
        A view to handle session based logging in
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"})
    if len(users) <= 0:
        return jsonify({"error": "no user found for this email"})
    user = users[0]
    if user.is_valid_password(password) is False:
        return jsonify({"error": "wrong password"})
    from api.v1.app import auth
    session_id = auth.create_session(getattr(user, 'id'))
    result = jsonify(user.to_json())
    result.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return result


@app_views.route(
        '/api/v1/auth_session/logout', methods=['DELETE'],
        strict_slashes=False)
def logout():
    """
        Logs out a user
    """
    from api.v1.app import auth
    is_destroyed = auth.destroy_session(request)
    if not is_destroyed:
        abort(404)
    return jsonify({})
