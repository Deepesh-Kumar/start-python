#import re
#b = re.compile(r'\d+\.\d+\.\d+.*?')
#e = 'Ross McFluff: 834.345.1254 155'
#c = b.search(e)
#print c.group()
#text = "Python for beginner is a very cool website"
#p = re.split('cool',text, flags=re.IGNORECASE)
#print p


#import os
#pwd = os.getcwd()
#for roots,dirs, files in os.walk("/Users/deepeshk/Documents"):
	#print files
	#print dirs	
	#print roots
#	for f in dirs:
#		print os.path.join(roots,f)

#import sys,os
#print 'sys.argv[0] =', sys.argv[0]            
#pathname = os.path.dirname(sys.argv[0])        
#print 'path =', pathname
#print 'full path =', os.path.abspath(pathname)


#def y(*args):
#	print type(args)


#def x(** kwargs):
#	print type(kwargs)


#x()
#y()



#def fnc2(arg1, arg2, *args, **kwargs):
 #  print('{} {} {} {}'.format(arg1, arg2, args, kwargs))

#print('fnc2()')
#fnc2() # error
#fnc2(1,2)
#fnc2(1,2,3,'haystack')
#fnc2(arg1=1, arg2=2, c=3)
#fnc2(arg1=1, arg2=2, c=3, d='Spark')
#fnc2(1,2,3, a=1, b=2)
#fnc2(*lst, **dct)
#fnc2(*tpl, **dct)
#fnc2(1,2,*tpl)
#fnc2(1,*tpl,d='nltk')
#fnc2(1,2,*tpl,d='scikit')






import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()
g = []
h = []
#print d['data']
k = []
l = []






class access:
	def __init__(self,IP,username,password):
		self.IP = IP
		self.username = username
		self.password = password
		#self.payload = payload
		#self.payload1 = payload1
		#self.g = []
		#self.h = []
		#self.k = []
		#self.l = []

	#def get_req(self):
	#	uri = 'https://' + self.IP + '/dataservice/device' 
	#	s = requests.session()
	#	response = s.get(uri, auth=HTTPBasicAuth(self.username, self.password), verify=False)
	#	d = response.json()
	#	print d['data']
	def post_req(self):
		uri = 'https://' + self.IP + '/dataservice/device' 
		s = requests.session()
		response = s.get(uri, auth=HTTPBasicAuth(self.username, self.password), verify=False)
		d = response.json()
		g = []
		h = []
        #print d['data']
        k = []
        l = []
        for i in d['data']:
        	if i['device-model'] == 'vedge-1000' and i['reachability'] == 'reachable' and i['personality'] =='vedge':
        		h.append(i['local-system-ip'])
        		g.append(i['uuid'])
        	elif i['device-model'] =='vedge-cloud' and i['reachability'] == 'reachable' and i['personality'] == 'vedge':
        		k.append(i['local-system-ip'])
        		l.append(i['uuid'])
        payload = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,"data":[{"family":"vedge-mips","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},"devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"}
        payload1 = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,"data":[{"family":"vedge-x86","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},"devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"}
        urv = 'https://10.195.168.110/dataservice/device/action/install'
        headers={'Content-Type': 'application/json'}
        for (i,j) in zip(g,h):
        	payload['devices'][0]['deviceId'] = i
        	payload['devices'][0]['deviceIP'] = j
        	q = json.dumps(payload)
        	response_post = s.post(urv, auth=HTTPBasicAuth(self.username, self.password), data = q, headers=headers, verify=False)
        	print response_post
        for (o,p) in zip(k,l):
        	payload1['devices'][0]['deviceId'] = p
        	payload1['devices'][0]['deviceIP'] = o
        	e = json.dumps(payload1)
        	response_post_new = s.post(urv, auth=HTTPBasicAuth(self.username, self.password), data = e, headers=headers, verify=False)
        	print response_post_new




a = access('10.195.168.110', 'deepesh', 'deepesh4321!')
res = a.post_req()
print res































































































