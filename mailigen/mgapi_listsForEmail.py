from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

email_address = my_email

retval = api.listsForEmail(email_address)
if api.errorCode:
	print "Unable to get lists ID!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned: "
	if isinstance(retval, dict):
		for id in retval.items():
			print "\tID = ", id
	elif isinstance(retval, list):
		for id in retval:
			print "\tID = ", id
