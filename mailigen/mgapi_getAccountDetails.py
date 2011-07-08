from lib.config import * #contains apikey
from lib.MGAPI import MGAPI

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)
retval = api.getAccountDetails()

if api.errorCode:
	print "Unable to get account info!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "Returned"
	for key,value in retval.items():
		if isinstance(value, dict):
			print "\t", key
			for k,v in value.items():
				if isinstance(v, dict):
					print "\t\t%d" % (k + 1)
					for k_,v_ in v.items():
						print "\t\t\t", k_, " = ", v_
				elif isinstance(v, list):
					print "\t\t%d" % (k + 1)
					for k_,v_ in enumerate(v):
						print "\t\t\t", k_, " = ", v_
				else:
					print "\t\t", k, " = ", v
		elif isinstance(value, list):
			print "\t", key
			for k,v in enumerate(value):
				if isinstance(v, dict):
					print "\t\t%d" % (k + 1)
					for k_,v_ in v.items():
						print "\t\t\t", k_, " = ", v_
				elif isinstance(v, list):
					print "\t\t%d" % (k + 1)
					for k_,v_ in enumerate(v):
						print "\t\t\t", k_, " = ", v_
				else:
					print "\t\t", k, " = ", v
		else:
			print "\t", key, " = ", value
