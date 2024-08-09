#!/usr/bin/env python3
"""
    Contains a class Auth that defines the apps authentication
"""
from .auth import Auth
import base64


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
