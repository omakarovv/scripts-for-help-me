#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


@app.route('/logs')
def log_reload():
    with open('/var/log/auth.log', 'rb') as f:
        return f.read(), 200, {'Content-Type': 'text; charset=utf-8'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
