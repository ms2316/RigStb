import urllib2, json

data = {}

#gather status of rigs 1 to 9
for rig in range(1,10):
	for stb in range(1,8):
		url = "http://testaut-" + str(rig) + "-switch-pc:10000/stb-" + str(stb)
		response = urllib2.urlopen(url)
		jdata = json.load(response)
		#validity check
		data["rig" + str(rig) + "stb" + str(stb)] = jdata

#gather status of rig 10




#test
tmp = data["rig3stb2"]
box = tmp['box']
print 'version: ' + box['cds_version']
print "ip: " + box["ip"]
print "mac: " + box["mac"]
print "model: " + box["model"]
print "oem: " + box["oem"]
print "ruid: " + box["ruid"]
print "variant: " + box["variant"]
	
	
