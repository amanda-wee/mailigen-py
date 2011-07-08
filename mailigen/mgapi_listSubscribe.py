from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
email_address = my_email
merge_vars = {'EMAIL': my_email, 'FNAME': 'Joe'} # or merge_vars = {}
email_type = 'html'
double_optin = True
update_existing = False
send_welcome = False

retval = api.listSubscribe(id, email_address, merge_vars, email_type, double_optin, update_existing, send_welcome)
if api.errorCode:
	print "Unable to load listSubscribe()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned: ", retval