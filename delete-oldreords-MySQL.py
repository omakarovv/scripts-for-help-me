#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

db = MySQLdb.connect(host="localhost",user="username",passwd="password",db="dbname")

cursor = db.cursor()

cursor.execute("DELETE FROM `tbl_name` WHERE ((`date` < (NOW() - INTERVAL 1 DAY)) AND `ip` NOT IN (''))")

#data = cursor.fetchone()
data = cursor.fetchall()
db.commit()
db.close()
