from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId

retval = api.campaignStats(cid)
if api.errorCode:
	print "Unable to load campaignStats()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Stats for ", cid
	for k,v in retval.items():
		print "\t", k, " => ", v
