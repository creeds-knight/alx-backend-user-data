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
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if path[-1] != '/':
            path = path + '/'
        for pa in excluded_paths:
            if pa == path:
                return False
        return True

    def authorization_header(self, request=None) -> TypeVar('User'):
        """
            Returns None
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Returns None
        """
        return None
