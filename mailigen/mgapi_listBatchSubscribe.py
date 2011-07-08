from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
batch = []
batch.append({'EMAIL': my_email, 'FNAME': 'Joe'})
batch.append({'EMAIL': boss_man_email, 'FNAME': 'Boss'})

double_optin = True
update_existing = False

retval = api.listBatchSubscribe(id, batch, double_optin, update_existing)
if api.errorCode:
	print "Unable to load listBatchSubscribe()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "success:", retval['success_count']
	print "errors:", retval['error_count']
	for val in retval['errors']:
		print "\t*", val['email'], " failed"
		print "\tcode:", val['code']
		print "\tmsg :", val['message']
