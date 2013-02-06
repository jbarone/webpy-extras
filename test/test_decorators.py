import web
from nose.tools import *

from extras.decorators import *

class TestDecorators():

    def test_login_requierd_fail(self):
        urls = (
            '/test', 'hello'
        )
        class hello:
            @login_required(lambda: False)
            def GET(self):
                assert False
        app = web.application(urls, locals())
        response = app.request('/test')
        eq_(response.status, '303 See Other')
        eq_(response.headers['Location'], 
            'http://0.0.0.0:8080/login?next=/test')

    def test_login_requierd_pass(self):
        urls = (
            '/test', 'hello'
        )
        class hello:
            @login_required(lambda: True)
            def GET(self):
                return 'test'
        app = web.application(urls, locals())
        response = app.request('/test')
        eq_(response.status, '200 OK')

    def test_csrf_protected_fail(self):
        session = {'csrf_token': 'test'}
        urls = (
            '/test', 'hello'
        )
        class hello:
            @csrf_protected(session)
            def POST(self):
                assert False
        app = web.application(urls, locals())
        response = app.request('/test', method='POST', 
                               data=dict(csrf_token='not test'))
        eq_(response.status, '400 Bad Request')

    def test_csrf_protected_pass(self):
        session = {'csrf_token': 'test'}
        urls = (
            '/test', 'hello'
        )
        class hello:
            @csrf_protected(session)
            def POST(self):
                return 'test'
        app = web.application(urls, locals())
        response = app.request('/test', method='POST', 
                               data=dict(csrf_token='test'))
        eq_(response.status, '200 OK')
