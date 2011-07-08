from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId
start = 0
limit = 1000

retval = api.campaignForwardStats(cid, start, limit)
if api.errorCode:
	print "Unable to load campaignForwardStats()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	if len(retval) == 0:
		print "No stats for this campaign yet!"
	else:
		for email, detail in retval.items():
			print "E-mail: ", email
			print "\tFriend name = ", detail['friend_name']
