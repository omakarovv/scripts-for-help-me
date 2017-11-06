#!/usr/bin/env python3
from flask import Flask, Response
import time
import os

app = Flask(__name__)

class log_presenter:

    def proccess(self):
        with open('test_log.log', 'r') as f:
            for line in f:
                yield "".join(line) + '\n'


log_viewer = log_presenter()

@app.route('/')

def present_log():
    return Response(log_viewer.proccess(), mimetype='text')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
