from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId

retval = api.campaignGeoOpens(cid)
if api.errorCode:
	print "Unable to load campaignGeoOpens()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Open from %d countries:" % (len(retval))
	for country in retval:
		print "\t", country['code'], "\t", country['name'], "\t", country['opens']
