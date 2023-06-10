import markdown
from config import myconfig

def introduction():
    with open(myconfig.get('rootpath') + '/README.md', 'r', encoding='utf-8') as f:
        text = f.read()
    return markdown.markdown(text)