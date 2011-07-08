from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId
start = 0
limit = 25

retval = api.campaignBounceMessages(cid, start, limit)
if api.errorCode:
	print "Unable to load campaignBounceMessages()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Messages returned: %d" % (len(retval))
	for msg in retval:
		print "%s - %s" % (msg['date'], msg['email'])
		print msg['message'][0:150]
