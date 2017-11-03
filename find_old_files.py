#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import re
import datetime


# Directory for search.
dir = '/home'

# REGEX for exclude path: dev,sys,proc.
pattern = re.compile('^\/[dev,proc,sys]\/*')

# Date and time now.
dnow = datetime.datetime.now()

# Begin search and create list files.
for root, dirs, files in os.walk(dir):
    for name in files:

        """
        - dirname  -> Get directory name
        - fullname -> fullpath to the file
        - filepath -> check existing file or directory
        """

        dirname = os.path.join(root)
        fullname = os.path.join(root, name)

#If dirname is pattern match do nothing.
        if pattern.match(dirname):
            continue

# Else check file exist and file size.
        else:
            if os.path.exists(fullname) and os.path.isfile(fullname):
                sz = os.path.getsize(fullname) / 1000 / 1000

                dmodify = (
                   datetime.datetime.fromtimestamp(os.path.getmtime(fullname))
                  )

                days_diff = (dnow-dmodify).days

                if sz > 100 and days_diff >= 30:
                    print('{} | Size is: {}Mb | Last Modified: {} Days ago'
                          .format(fullname, round(sz, 2), days_diff))
