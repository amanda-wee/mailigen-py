from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId
start = 0
limit = 1000

retval = api.campaignHardBounces(cid, start, limit)
if api.errorCode:
	print "Unable to load campaignHardBounces()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "E-mails returned: %d" % (len(retval))
	for email in retval:
		print "\t", email
