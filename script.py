import urllib2
import json
import model
import sqlalchemy
from sqlalchemy.orm import sessionmaker

#Returns url of the given rig/stb
def get_url(rig, stb):
	if rig == 10:
		return "http://testaut-10-switch-pc-1:10000/stb-" + str(stb)
	else:
		return "http://testaut-" + str(rig) + "-switch-pc:10000/stb-" + str(stb)

#Gets stb status and throws HTTPError exception
def get_stb_status(rig, stb):
	#try:
	response = urllib2.urlopen( get_url(rig, stb) )
	jdata = json.load(response)
	return jdata
	#except urllib2.HTTPError:
	#	return "Invalid rig/stb"

def save_machine_status():
	#Establish connection with db
	engine = model.create_engine('postgresql://stb-tester:testaut@localhost:57998/testaut', echo = True)
	Session = sessionmaker(bind = engine)
	session = Session() #establish a connection

	#gather status of rigs 1 to 10
	for rig in range(1,13):
		for stb in range(1,8):
			try:
				jdata = get_stb_status(rig,stb)
				#Convert jdata to Stb
				#Save to database
			except Exception:
				#get_stb_status() returned with an error
				pass

	session.commit()
	session.close()
#test
save_machine_status()

tmp =  get_stb_status(1,8)
box = tmp['box']
print 'version: ' + box['cds_version']
print "ip: " + box["ip"]
print "mac: " + box["mac"]
print "model: " + box["model"]
print "oem: " + box["oem"]
print "ruid: " + box["ruid"]
print "variant: " + box["variant"]
