from lib.config import * #contains apikey
from lib.MGAPI import MGAPI
import base64

# This Example shows how to ping using the MGAPI.php class and do some basic error checking.

api = MGAPI(apikey)


type = 'html'

options = {
	'list_id': listId,
	'subject': 'Test Newsletter Subject',
	'from_email': 'example@example.org',
	'from_name': 'DEMO, Inc.',
	'tracking': {
		'opens': True,
		'html_clicks': True,
		'text_clicks': False
	},
	'analytics': {
		'google': 'my_google_analytics_key'
	},
	'title': 'Test Newsletter Title'
}

content = {
	#'template_id': 'template_id',
	#'html': 'some pretty html content *[UNSUB]* message',
	#'plain': 'some pretty plain content *[UNSUB]* message',
	#'url': 'http://www.google.com',
	'archive': base64.encodestring(open('archive.zip').read()),
	'archive_type': 'zip'
}

retval = api.campaignCreate(type, options, content)
if api.errorCode:
	print "Unable to load campaignCreate()!"
	print "\tCode=", api.errorCode
	print "\tMsg=", api.errorMessage
else:
	print "New Campaign ID:", retval
