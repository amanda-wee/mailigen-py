from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
email_address = my_email
delete_member = False
send_goodbye = True
send_notify = False

retval = api.listUnsubscribe(id, email_address, delete_member, send_goodbye, send_notify)
if api.errorCode:
	print "Unable to load listUnsubscribe()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned: ", retval