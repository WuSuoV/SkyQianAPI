import random

meta = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=~,./<>?"


def passwd(num: int):
    return ''.join(random.choices(meta, k=num))

