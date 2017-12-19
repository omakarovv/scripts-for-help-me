#!/usr/bin/env python3

import os
import time

pid = os.getpid()
pid_file = "pid_file"

def is_proccess_running():
    if not os.path.exists(pid_file):
        return True
    else:
       old_pid_file = open(pid_file, 'r')
       old_pid = int(old_pid_file.readline())
       try:
           check_old_pid = os.kill(old_pid, 0)
       except:
           return True
           
if is_proccess_running():
    with open(pid_file, 'w') as f:
        f.write(str(pid))

    try:
        x = 30
        while x > 0:
            time.sleep(5)
            x -= 1
            print(pid)
    except:
        raise
    finally:
        os.remove(pid_file)
