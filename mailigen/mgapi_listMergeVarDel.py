from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
tag = 'MERGE_TAG'

retval = api.listMergeVarDel(id, tag)
if api.errorCode:
	print "Unable to load listMergeVarDel()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned: ", retval