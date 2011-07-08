from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

username = "username"
password = "password"

retval = api.apikeyAdd(username, password)
if api.errorCode:
	print "Unable to add new API key!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned new API key: ", retval
