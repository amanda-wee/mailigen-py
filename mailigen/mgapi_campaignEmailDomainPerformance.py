from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

cid = campaignId

retval = api.campaignEmailDomainPerformance(cid)
if api.errorCode:
	print "Unable to load campaignEmailDomainPerformance()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	if len(retval) == 0:
		print "No Email Domain stats yet!"
	else:
		for domain in retval:
			print domain['domain']
			print "\tEmails: ", domain['emails']
			print "\tOpens: ", domain['opens']
			print "\tClicks: ", domain['clicks']
			
