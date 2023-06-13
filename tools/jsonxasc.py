import json

from flask import Response


def jsonxasc(adict: dict):
    return Response(json.dumps(adict, ensure_ascii=False, sort_keys=False, indent=4),
                    content_type='application/json;charset=utf-8')
