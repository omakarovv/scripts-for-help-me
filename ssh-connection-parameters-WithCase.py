#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
key_path = '/path/to/key'
port = <port_namber>
user = 'user_name'

def switch_case(case):
    return {
    '1' : "1.1.1.1",
    '2' : "2.2.2.2",
}.get(case, "You enter number is out of range")

num = raw_input('''Input a number:
1. server1
2. server2 \n''')

if switch_case(num) == "1.1.1.1" or switch_case(num) == "2.2.2.2":
    print ('ssh -i %s -p %d %s@'+switch_case(num)) %(key_path, port, user)
