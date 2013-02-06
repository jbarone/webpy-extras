import web

def login_required(logged_in, path='/login'):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            if not logged_in():
                raise web.seeother(path + '?next=' + web.ctx.get('path', '/'))
            else:
                return f(*args, **kwargs)
        return wrapped_f
    return wrap

def csrf_protected(session, token='csrf_token'):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            inputs = web.input(_unicode=False)
            if not (inputs.has_key(token) and
                    inputs.get(token) == session.pop(token, None)):
                raise web.badrequest()
            return f(*args, **kwargs)
        return wrapped_f
    return wrap
