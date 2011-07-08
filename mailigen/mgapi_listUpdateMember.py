from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)

id = listId
email_address = my_email
merge_vars = {"FNAME": 'Richard', "LNAME": 'Wright'}
email_type = 'html'

retval = api.listUpdateMember(id, email_address, merge_vars, email_type)
if api.errorCode:
	print "Unable to load listUpdateMember()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned: ", retval