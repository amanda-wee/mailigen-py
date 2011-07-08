from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId;

retval = api.listGrowthHistory(id)
if api.errorCode:
	print "Unable to load listGrowthHistory()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	for history in retval:
		print history['month']
		print "\tExisting=", history['existing']
		print "\tImports=", history['imports']