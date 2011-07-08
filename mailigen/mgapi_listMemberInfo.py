from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
email_address = my_email

retval = api.listMemberInfo(id, email_address)
if api.errorCode:
	print "Unable to load listMemberInfo()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	for k,v in retval.items():
		if isinstance(v, dict):
			#handle the merges
			for l,w in v.items():
				print "\t", l, " = ", w
		elif isinstance(v, list):
			#handle the merges
			for l,w in enumerate(v):
				print "\t", l, " = ", w
		else:
			print k, " = ", v
