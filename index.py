# -*- coding: utf-8 -*-

HELLO_WORLD = b"Hello world!\n"


class AppClass:
    """Produce the same output, but using a class
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield HELLO_WORLD


def handler(environ, start_response):
    return AppClass(environ, start_response)
