#!/usr/bin/env python3
import time

with open('test_log.log', 'r') as f:
    while 1:
        position = f.tell()
        line = f.readline()
        if not line:
            time.sleep(1)
            f.seek(position)
        else:
            print(line)
