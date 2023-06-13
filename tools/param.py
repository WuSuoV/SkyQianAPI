from flask import request


def param_value(key):
    method = request.method
    if method == 'GET':
        return request.args.get(key)

    if method == 'POST':
        rtype = request.content_type
        if rtype.startswith('application/json'):
            return request.json.get(key)
        elif rtype.startswith('application/form-data'):
            return request.form.get(key)
        else:
            return request.values.get(key)
