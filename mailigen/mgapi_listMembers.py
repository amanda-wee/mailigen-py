from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
status = "subscribed"
start = 0
limit = 500

retval = api.listMembers(id, status, start, limit)
if api.errorCode:
	print "Unable to load listMembers()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Members returned: ", len(retval)
	if isinstance(retval, dict):
		for member in retval.items():
			print "\t%s - %s" % (member['email'], member['timestamp'])
	elif isinstance(retval, list):
		for member in retval:
			print "\t%s - %s" % (member['email'], member['timestamp'])
