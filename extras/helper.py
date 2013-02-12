#!/usr/bin/env python
"""
Helper functions
"""

import web

__version__ = "0.1"
__author__ = ["Joshua Barone <jbarone@justbecausesoftware.com>"]

def csrf_token(session, token='csrf_token'):
    """
    Utility function to protect POST functions and
    provide a proper csrf token.

    This protects against cross site request forgery.

    >>> import tempfile
    >>> session = web.session.Session(None, web.session.DiskStore(tempfile.mkdtemp()))
    >>> session.csrf_token = 'test'
    >>> csrf_token(session)
    'test'
    >>> session._cleanup()
    >>> session = web.session.Session(None, web.session.DiskStore(tempfile.mkdtemp()))
    >>> csrf_token(session) == session.csrf_token
    True
    >>> session._cleanup()
    """
    if not session.has_key(token):
        from uuid import uuid4
        session.csrf_token = uuid4().hex
    return session.csrf_token
