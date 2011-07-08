from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)
retval = api.campaignTemplates()


if api.errorCode:
	print "Unable to load campaignTemplates()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Your templates:"
	for tmpl in retval:
		print "\t", tmpl['id'], " - ", tmpl['name'], " - ", tmpl['layout']
