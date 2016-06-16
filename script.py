import urllib2
import json
import model
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Returns url of the given rig/stb
def get_url(rig, stb):
	if rig == 10:
		return "http://testaut-10-switch-pc-1:10000/stb-" + str(stb)
	else:
		return "http://testaut-" + str(rig) + "-switch-pc:10000/stb-" + str(stb)

#Creates Stb model object from jdata+rig_no+stb_no
def json_to_stb(jdata, rig, stb):
	return model.Stb(
	rig_no = rig,
	stb_no = stb,
	version = jdata['box']['cds_version'],
	ip = jdata['box']['ip'],
	mac = jdata['box']['mac'],
	model = jdata['box']['model'],
	oem = jdata['box']['oem'],
	ruid = jdata['box']['ruid'],
	variant = jdata['box']['variant']
	)

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
	engine = create_engine('postgresql://stb-tester:testaut@localhost:57998/testaut', echo = False)
	Session = sessionmaker(bind = engine)
	session = Session() #establish a connection

	#gather status of rigs 1 to 10
	for rig in range(1,13):
		for stb in range(1,10):
			try:
				jdata = get_stb_status(rig,stb)
				#Convert jdata to Stb
				#Save to database
				session.add( json_to_stb(jdata, rig, stb) )
			except Exception:
				print "Exception processing stb " + str(stb) + " in rig " + str(rig)

	session.commit()
	session.close()

#test
#save_machine_status()
'''
tmp =  get_stb_status(1,8)
box = tmp['box']
print 'version: ' + box['cds_version']
print "ip: " + box["ip"]
print "mac: " + box["mac"]
print "model: " + box["model"]
print "oem: " + box["oem"]
print "ruid: " + box["ruid"]
print "variant: " + box["variant"]
'''
