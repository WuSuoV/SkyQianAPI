import functools

from flask import request


class Token:
    token: list

    def __init__(self, token):
        self.token = token

    def verify_token(self, func):
        @functools.wraps(func)
        def func_new(*args, **kwargs):
            token = request.args.get('token')
            if token in self.token:
                return func(*args, **kwargs)
            else:
                return 'Token is invalid.'

        return func_new
