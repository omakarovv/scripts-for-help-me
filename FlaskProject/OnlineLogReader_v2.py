#!/usr/bin/env python3
from flask import Flask, Response
import time

app = Flask(__name__)

def collect_rows():
    with open('test_log.log', 'r') as f:
        while 1:
            where = f.tell()

            if os.stat('test_log.log').st_size == 0:
                where = 0

            line = f.readline()

            if not line:
                f.seek(where)
            else:
                yield "".join(line) + '\n'

@app.route('/')

def present_log():
    return Response(collect_rows(), mimetype='text')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

