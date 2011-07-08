from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId
test_emails = [my_email, boss_man_email]


retval = api.campaignSendTest(cid, test_emails)
if api.errorCode:
	print "Unable to load campaignSendTest()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Campaign Tests Sent!"
