import json


def jsonxasc(ajson):
    return json.dumps(ajson, ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ':　'))
