from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId

retval = api.campaignClickStats(cid)
if api.errorCode:
	print "Unable to load campaignClickStats()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	if len(retval) == 0:
		print "No stats for this campaign yet!"
	else:
		for url, detail in retval.items():
			print "URL: %s" % (url)
			print "\tClicks = %s" % (detail['clicks'])
			print "\tUnique Clicks = %s" % (detail['unique'])

