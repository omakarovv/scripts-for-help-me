#!/usr/bin/env python3
from flask import Flask, Response

app = Flask(__name__)

def iter_all_rows():
    with open('/var/log/auth.log', 'r') as f:
        for line in f:
            yield "".join(line) + '\n'

@app.route('/')
def generate_log():
    return Response(iter_all_rows(), mimetype='text')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
