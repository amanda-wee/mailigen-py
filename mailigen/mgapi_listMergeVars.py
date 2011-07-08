from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId

retval = api.listMergeVars(id)
if api.errorCode:
	print "Unable to load listMergeVars()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Merge tags returned: ", len(retval)
	if isinstance(retval, dict):
		for i,var in retval.items():
			print "Var #%d:" % (i)
			print "\tTag: ", var['tag']
			print "\tName: ", var['name']
			print "\tRequired: ", var['req']
	elif isinstance(retval, list):
		for i,var in enumerate(retval):
			print "Var #%d:" % (i)
			print "\tTag: ", var['tag']
			print "\tName: ", var['name']
			print "\tRequired: ", var['req']
