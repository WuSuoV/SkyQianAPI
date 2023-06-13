import json


def jsonxasc(ajson):
    return '<pre>' + json.dumps(ajson, ensure_ascii=False, sort_keys=False, indent=4,
                                separators=(', ', ':　')) + '</pre>'
