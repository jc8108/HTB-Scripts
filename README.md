# HTB-Scripts
One-off scripts I've made for HackTheBox rooms and challenges

SNIPER - this room had a login / registration page with a LFI vulnerabilitity
  - while looking at files on the system discover some commands arent working
  - this script helps find the bad characters that are getting filtered
  - posting here to provide framework for similiar attack

Emdee five for life - this room gives you a string and wants the hash back for the flag, submitting manually is too slow so we need to script it
  - pretty straight forward when using beautiful soup 
  - create session, parse the request, find the string, hash it, and send it back and parse out the flag

Phonebook - login page with a XSS for a distraction in the URL, fuzzing login page shows the * wildcard allows logins
  - this script is over-coded, could have been done in a dirty and quick manner just to get flag
  - tries every character with and without wildcard until it finds username and password
