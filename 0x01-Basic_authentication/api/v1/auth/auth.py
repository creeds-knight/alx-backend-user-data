#!/usr/bin/env python3
"""
    Contains a class Auth that defines the apps authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
        A class Auth to manage Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Returns False -path and excluded_paths
        """
        return False

    def authorization_header(self, request=None) -> TypeVar('User'):
        """
            Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Returns None
        """
        return None
