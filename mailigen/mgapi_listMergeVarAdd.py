from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
tag = 'MERGE_TAG'
name = 'Merge Tag name'
options = {
	"field_type": 'text',
	"req": False,
	"default_value": 'Default value',
	"show": True
}

retval = api.listMergeVarAdd(id, tag, name, options)
if api.errorCode:
	print "Unable to load listMergeVarAdd()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned: ", retval