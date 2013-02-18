#!/usr/bin/env python
"""
Decorators for use in web.py classes.
"""

import web

__version__ = "0.1"
__author__ = ["Joshua Barone <jbarone@justbecausesoftware.com>"]


def login_required(logged_in, path='/login'):
    """
    Will ensure that a user is logged in to the system before allowing them
    to access the page/resource they are attempting to. If not logged in,
    the user is redirected to the login page.

    :param logged_in boolean function that determines if the user is logged in
    :param path the path to the login page (default: '/login')
    """
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            if not logged_in():
                raise web.seeother(path + '?next=' + web.ctx.get('path', '/'))
            else:
                return f(*args, **kwargs)
        return wrapped_f
    return wrap

def csrf_protected(session, token='csrf_token'):
    """
    Will ensure that a correct csrf token is provided in a POST.

    :param session function to get the session collection
    :param token the name of the token in the form
    """
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            inputs = web.input(_unicode=False)
            if not (inputs.has_key(token) and
                    inputs.get(token) == session().pop(token, None)):
                raise web.badrequest()
            return f(*args, **kwargs)
        return wrapped_f
    return wrap
