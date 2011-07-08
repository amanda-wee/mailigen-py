from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

username = "username"
password = "password"
expired = False

retval = api.apikeys(username, password, expired)
if api.errorCode:
	print "Unable to get API keys!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "All API Keys for your account:"
	for key in retval:
		print "key = ", key['apikey']
		print "\tcreated: = ", key['created_at']
		print "\texpired: = ", key['date_expired']
