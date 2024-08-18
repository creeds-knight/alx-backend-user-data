#!/usr/bin/ env python3
"""
    An Authentication provider(authentication backend)
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
        Hashes a password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
