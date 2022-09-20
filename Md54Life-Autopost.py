import requests
import hashlib
from bs4 import BeautifulSoup

erl = "http://138.68.157.75:31655"

# create session, use bs4 to parse html
sesh = requests.session()

r = sesh.get(erl)

soup = BeautifulSoup(r.content, "html.parser")

# from Burp we see hash is in the H3 flag so create a bs4 element
emdee = soup.find("h3")

# parse string from the bs4 element
for t in emdee:
	tag = t

# from Burp we see the hash is passed as parameter "hash"
mdhash = hashlib.md5(bytes(t, 'utf-8')).hexdigest()

fields = {"hash":mdhash}

r = sesh.post(erl, fields)

# originally I used r.text to retrieve HTML and find flag, then created this to make it pretty
# if it says too slow, just run it again 
soup = BeautifulSoup(r.content, "html.parser")
flag = soup.find("p")

for f in flag:
	print(f)