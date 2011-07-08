from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)
retval = api.campaigns()


if api.errorCode:
	print "Unable to load campaigns()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "%d Campaigns Returned:" % (len(retval))
	for c in retval:
		print "Campaign Id: %s - %s" % (c['id'], c['title'])
		print "\tStatus: %s - type = %s" % (c['status'], c['type'])
		print "\tsent: %s to %s members" % (c['send_time'], c['emails_sent'])
