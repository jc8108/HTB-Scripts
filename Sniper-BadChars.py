import requests
import string
import random

erl = "http://10.10.10.151"
login = f"{erl}/user/login.php"
register = f"{erl}/user/registration.php"
bad = []

# creates this list of characters to test !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
char = string.punctuation

print(f"Registering {len(char)} usernames and making requests...")

for c in char:
	test = "CHANGEME" + c
	rfields = {"email":"e@mail.com", "username":test, "password":test, "submit":" "}
	lfields = {"username":test, "password":test, "submit": " "}
	r = requests.post(register, data = rfields)
	r = requests.post(login, data = lfields)
	if "incorrect." in r.text:
		print(c)
		bad.append(c)

print(f"Found {len(bad)} characters:")
print("".join(bad))

#change the test variable each time you re-run this to prevent false positives 
