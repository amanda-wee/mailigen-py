from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId
name = 'title'
value = 'New Title'


retval = api.campaignUpdate(cid, name, value)
if api.errorCode:
	print "Unable to load campaignUpdate()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "SUCCESS!"
