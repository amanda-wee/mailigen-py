from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)
retval = api.lists()


if api.errorCode:
	print "Unable to load lists()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Lists returned: %d" % (len(retval))
	for list in retval:
		print "Id = %s - %s" % (list["id"], list["name"])
