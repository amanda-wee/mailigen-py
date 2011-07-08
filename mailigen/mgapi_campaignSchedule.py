from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId
schedule_time = '2020-05-18 11:59:21'


retval = api.campaignSchedule(cid, schedule_time)
if api.errorCode:
	print "Unable to load campaignSchedule()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Campaign Scheduled to be delivered %s!" % (schedule_time)
