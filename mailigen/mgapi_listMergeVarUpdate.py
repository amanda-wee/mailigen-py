from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
tag = 'MERGE_TAG'
options = {
	"req": False,
	"name": 'Merge Tag name',
	"default_value": 'Default value',
	"show": True
}

retval = api.listMergeVarUpdate(id, tag, options)
if api.errorCode:
	print "Unable to load listMergeVarUpdate()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned: ", retval