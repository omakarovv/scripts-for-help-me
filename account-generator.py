#!/usr/bin/env python3
import random
import string
import pymysql

dbserver = "localhost"
dbuser = "username"
dbpassword = "password"
dbname = "dbname"
domain_name = "@example.com"

user_prefix = str(input("Input prefix:"))

conn = pymysql.connect(host=dbserver, user = dbuser, passwd = dbpassword, db= dbname, autocommit=True)
cur = conn.cursor()

cur.execute("SELECT * FROM virtual_users WHERE user LIKE %s", user_prefix+"%")
for response in cur:
    print(response)

start_number = int(input("Input start number:"))
end_number = int(input("Input end number:"))

def create_account(end_number):
    for i in range(start_number, end_number + 1):
        account = "%s-%d" % (user_prefix, i)

        characters = string.ascii_letters + string.punctuation  + string.digits

        upassword =  "".join(random.choice(characters) for x in range(random.randint(6, 8)))

        cur.execute("INSERT INTO virtual_users (domain_id, password, user) VALUES (1, SHA2('%s', 256), '%s@example.com');" % (upassword, account))

        print(account + domain_name + " ", " " + upassword, sep=":")

create_account(end_number)

cur.close()
conn.close()
