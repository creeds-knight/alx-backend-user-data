#!/usr/bin/env python3
"""
    Contains a class Auth that defines the apps authentication
"""
from .auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
        Performs Basic authentication
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
            Returns the Base63 part of the Authorisation header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
            ) -> str:
        """
            Decoding in base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """
            Basic-User credentials
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        try:
            email, password = decoded_base64_authorization_header.split(":")
        except Exception:
            return (None, None)
        return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """
            Basic user object
        """
        from models.user import User
        if not isinstance(user_email, str) or user_email is None:
            return None
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        user = users[0]
        if user.is_valid_password(user_pwd) is True:
            return user
        else:
            return None

