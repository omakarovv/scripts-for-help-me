#!/usr/bin/env python3
import time
import os

with open('test_log.log', 'r') as f:
    while 1:
        where = f.tell()

        if os.stat('test_log.log').st_size == 0:
            where = 0

        line = f.readline()
        if not line:
            time.sleep(1)
            f.seek(where)
        else:
            print(line)
