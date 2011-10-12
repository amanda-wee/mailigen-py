import urlparse
import urllib
import socket
import json

class MGAPI:
	version = "1.0"
	errorMessage = ""
	errorCode = 0

	# API server adrese
	apiUrl = ""

	# Default to a 300 second timeout on server calls
	timeout = 300

	# Default to a 8K chunk size
	chunkSize = 8192
	
	# Lietotaja API atslega
	api_key = ""
	
	def __init__(self, apikey=None, secure=False):
		self.secure = secure
		self.api_key = apikey
		self.apiUrl = urlparse.urlparse("http://api.mailigen.com/" + self.version + "/?output=json")
	
	def setTimeout(self, seconds):
		if isinstance(seconds, int):
			self.timeout = seconds
			return True

	def getTimeout(self):
		return self.timeout

	def useSecure(self, val):
		if val is True:
			self.secure = True
		else:
			self.secure = False
	
	#
	def campaignUnschedule(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignUnschedule", params)
		
	#
	def campaignSchedule(self, cid, schedule_time):
		params = {}
		params["cid"] = cid
		params["schedule_time"] = schedule_time
		return self.callServer("campaignSchedule", params)
		
	#
	def campaignResume(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignResume", params)
		
	#
	def campaignPause(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignPause", params)
		
	#
	def campaignSendNow(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignSendNow", params)
		
	#
	def campaignSendTest(self, cid, test_emails = {}, send_type = None):
		params = {}
		params["cid"] = cid
		params["test_emails"] = test_emails
		params["send_type"] = send_type
		return self.callServer("campaignSendTest", params)
		
	#
	def campaignTemplates(self):
		params = {}
		return self.callServer("campaignTemplates", params)
		
	#
	def campaignCreate(self, type, options, content, type_opts = None):
		params = {}
		params["type"] = type
		params["options"] = options
		params["content"] = content
		params["type_opts"] = type_opts
		return self.callServer("campaignCreate", params)
		
	#
	def campaignUpdate(self, cid, name, value):
		params = {}
		params["cid"] = cid
		params["name"] = name
		params["value"] = value
		return self.callServer("campaignUpdate", params)
		
	#
	def campaignReplicate(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignReplicate", params)
		
	#
	def campaignDelete(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignDelete", params)
		
	#
	def campaigns(self, filters = {}, start = 0, limit = 25):
		params = {}
		params["filters"] = filters
		params["start"] = start
		params["limit"] = limit
		return self.callServer("campaigns", params)
		
	#
	def campaignStats(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignStats", params)
		
	#
	def campaignClickStats(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignClickStats", params)
		
	#
	def campaignEmailDomainPerformance(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignEmailDomainPerformance", params)
		
	#
	def campaignHardBounces(self, cid, start = 0, limit = 1000):
		params = {}
		params["cid"] = cid
		params["start"] = start
		params["limit"] = limit
		return self.callServer("campaignHardBounces", params)
		
	#
	def campaignSoftBounces(self, cid, start = 0, limit = 1000):
		params = {}
		params["cid"] = cid
		params["start"] = start
		params["limit"] = limit
		return self.callServer("campaignSoftBounces", params)
		
	#
	def campaignUnsubscribes(self, cid, start = 0, limit = 1000):
		params = {}
		params["cid"] = cid
		params["start"] = start
		params["limit"] = limit
		return self.callServer("campaignUnsubscribes", params)
		
	#
	def campaignGeoOpens(self, cid):
		params = {}
		params["cid"] = cid
		return self.callServer("campaignGeoOpens", params)
		
	#
	def campaignForwardStats(self, cid, start = 0, limit = 1000):
		params = {}
		params["cid"] = cid
		params["start"] = start
		params["limit"] = limit
		return self.callServer("campaignForwardStats", params)
		
	#
	def campaignBounceMessages(self, cid, start = 0, limit = 25):
		params = {}
		params["cid"] = cid
		params["start"] = start
		params["limit"] = limit
		return self.callServer("campaignBounceMessages", params)
	
	#
	def lists(self):
		params = {}
		return self.callServer("lists", params)
	
	#
	def listMergeVars(self, id):
		params = {}
		params["id"] = id
		return self.callServer("listMergeVars", params)
	
	#
	def listMergeVarAdd(self, id, tag, name, options = {}):
		params = {}
		params["id"] = id
		params["tag"] = tag
		params["name"] = name
		params["options"] = options
		return self.callServer("listMergeVarAdd", params)
	
	#
	def listMergeVarUpdate(self, id, tag, options):
		params = {}
		params["id"] = id;
		params["tag"] = tag;
		params["options"] = options;
		return self.callServer("listMergeVarUpdate", params)

	def listMergeVarDel(self, id, tag):
		params = {}
		params["id"] = id
		params["tag"] = tag
		return self.callServer("listMergeVarDel", params)
		
	#
	def listSubscribe(self, id, email_address, merge_vars, email_type = 'html', double_optin = True, update_existing = False, send_welcome = False):
		params = {}
		params["id"] = id
		params["email_address"] = email_address
		params["merge_vars"] = merge_vars
		params["email_type"] = email_type
		params["double_optin"] = double_optin
		params["update_existing"] = update_existing
		params["send_welcome"] = send_welcome
		return self.callServer("listSubscribe", params)
		
	#
	def listUnsubscribe(self, id, email_address, delete_member = False, send_goodbye = True, send_notify = True):
		params = {}
		params["id"] = id
		params["email_address"] = email_address
		params["delete_member"] = delete_member
		params["send_goodbye"] = send_goodbye
		params["send_notify"] = send_notify
		return self.callServer("listUnsubscribe", params)
		
	#
	def listUpdateMember(self, id, email_address, merge_vars, email_type = ''):
		params = {}
		params["id"] = id
		params["email_address"] = email_address
		params["merge_vars"] = merge_vars
		params["email_type"] = email_type
		return self.callServer("listUpdateMember", params)
		
	#
	def listBatchSubscribe(self, id, batch, double_optin = True, update_existing = False):
		params = {}
		params["id"] = id
		params["batch"] = batch
		params["double_optin"] = double_optin
		params["update_existing"] = update_existing
		return self.callServer("listBatchSubscribe", params)
		
	#
	def listBatchUnsubscribe(self, id, emails, delete_member = False, send_goodbye = True, send_notify = False):
		params = {}
		params["id"] = id
		params["emails"] = emails
		params["delete_member"] = delete_member
		params["send_goodbye"] = send_goodbye
		params["send_notify"] = send_notify
		return self.callServer("listBatchUnsubscribe", params)
		
	#
	def listMembers(self, id, status = 'subscribed', start = 0, limit = 100):
		params = {}
		params["id"] = id
		params["status"] = status
		params["start"] = start
		params["limit"] = limit
		return self.callServer("listMembers", params)
		
	#
	def listMemberInfo(self, id, email_address):
		params = {}
		params["id"] = id
		params["email_address"] = email_address
		return self.callServer("listMemberInfo", params)
		
	#
	def listGrowthHistory(self, id):
		params = {}
		params["id"] = id
		return self.callServer("listGrowthHistory", params)
		
	#
	def getAccountDetails(self):
		params = {}
		return self.callServer("getAccountDetails", params)
		
	#
	def listsForEmail(self, email_address):
		params = {}
		params["email_address"] = email_address
		return self.callServer("listsForEmail", params)
		
	#
	def apikeys(self, username, password, expired = False):
		params = {}
		params["username"] = username
		params["password"] = password
		params["expired"] = expired
		return self.callServer("apikeys", params)
		
	#
	def apikeyAdd(self, username, password):
		params = {}
		params["username"] = username
		params["password"] = password
		return self.callServer("apikeyAdd", params)
		
	def apikeyExpire(self, username, password):
		params = {}
		params["username"] = username
		params["password"] = password
		return self.callServer("apikeyExpire", params)
	
	#
	def login(self, username, password):
		params = {}
		params["username"] = username
		params["password"] = password
		return self.callServer("login", params)

	#
	def ping(self):
		params = {}
		return self.callServer("ping", params)
	
	#
	def callServer(self, method, params):
		host = self.apiUrl.netloc
		params["apikey"] = self.api_key
		
		self.errorMessage = ""
		self.errorCode = ""
		post_vars = self.httpBuildQuery(params, key = None, encode = True)

		payload = "POST " + (self.apiUrl.path) + "?" + (self.apiUrl.query) + "&method=" + method + " HTTP/1.0\r\n" + \
			  "Host: " + host + "\r\n" + \
			  "User-Agent: MGAPI/" + self.version + " Python\r\n" + \
			  "Content-type: application/x-www-form-urlencoded\r\n" + \
			  "Content-length: %d\r\n" % (len(post_vars)) + \
			  "Connection: close \r\n\r\n" + \
			  post_vars
		
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			if self.secure:
				sock.connect(("ssl://" + host, 443))
			else:
				sock.connect((host, 80))
		except socket.error as msg:
			self.errorMessage = "Could not connect (socket.error: %s)" % msg
			self.errorCode = "-99"
			return False
		
		response = ""
		sock.send(payload)
		sock.settimeout(self.timeout)
		while 1:
			data = sock.recv(1024)
			if not data:
				break
			else:
				response += data
		sock.close()
		
		[throw, response] = response.split("\r\n\r\n", 2)
		
		serial = json.loads(response)
		if response and serial is None:
			response = {"error": "Bad Response.  Got This: "  + response, "code": "-99"}
		else:
			response = serial
		
		if isinstance(response, dict) and "error" in response:
			self.errorMessage = response["error"]
			self.errorCode = response["code"]
			return False
		
		return response

	#
	def httpBuildQuery(self, params, key=None, encode=False):
		ret = {}
		for name, val in params.items():
			if key is not None and not isinstance(key, int):
				name = "%s[%s]" % (key, name)
			
			if isinstance(val, dict):
				ret.update(self.httpBuildQuery(val, name))
			elif isinstance(val, list):
				ret.update(self.httpBuildQuery(dict(enumerate(val)), name))
			elif val is not None:
				ret[name] = val
		
		if encode is True:
			return urllib.urlencode(ret, doseq=True)
		else:
			return ret
