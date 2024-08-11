#!/usr/bin/env python3
"""
    A module to handle session Authentication
"""
from .auth import Auth
import uuid
from models.user import User
from flask import request


class SessionAuth(Auth):
    """
        A class to handle session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
            Creates a session_id_for a user
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            Return user id based on a session id
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        user_id = self.user_id_by_session_id.get(session_id, None)
        return user_id

    def current_user(self, request=None):
        """
            Returns a user based on the cookie value
        """
        user_id = self.user_id_for_session_id(self.session_cookie
                                              (request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
            Destroys a users session
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if (request is None or session_id is None) or user_id is None:
            return False
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
        return True

