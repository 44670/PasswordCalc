import base64

with open('index.html', 'r', encoding='utf8') as f:
    html = f.read()
b64Url = 'data:text/html;charset=UTF8;base64,' + base64.b64encode(html.encode('utf8')).decode('utf8')

with open('url.txt', 'w', encoding='utf8') as f:
    f.write(b64Url)