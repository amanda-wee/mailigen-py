from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId;
emails = [my_email, boss_man_email]
delete_member = False
send_goodbye = True
send_notify = False

retval = api.listBatchUnsubscribe(id, emails, delete_member, send_goodbye, send_notify)
if api.errorCode:
	print "Unable to load listBatchUnsubscribe()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "success:", retval['success_count']
	print "errors:", retval['error_count']
	for val in retval['errors']:
		print "\t*", val['email'], " failed"
		print "\tcode:", val['code']
		print "\tmsg :", val['message']
