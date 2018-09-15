import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()



#print  g
#print h
#p = {"action":"install","input":{"vEdgeVPN":0,"vSmartVPN":0,
#            "data":[{"family":"vedge-mips","version":"18.3.0"}],"versionType":"vmanage","reboot":True,"sync":True},
 #           "devices":[{"deviceIP":" ","deviceId":''}],"deviceType":"vedge"}

#urv = 'https://10.195.168.110/dataservice/template/device/config/attachcli'
#query = {'startDate':'2018-09-10T12:00:00','endDate':'2018-09-10T13:00:00','count':'10000'}
#headers={'Content-Type': 'application/json'}
#p = {"deviceTemplateList":[{"templateId":"e66e3f90-8c2b-414b-bd41-51c1bb2bf743","device":[{"csv-status":"complete","csv-deviceId":"11OD152130107","csv-deviceIP":"1.1.1.1",
#     "csv-host-name":"vE1-DC1","csv-templateId":"e66e3f90-8c2b-414b-bd41-51c1bb2bf743","selected":"true"}],"isEdited":"false"}]}
#headers={'Content-Type': 'application/json'}
#q = json.dumps(p)
#response_get = s.post(urv, auth=HTTPBasicAuth('deepesh', 'deepesh4321!'), data=q, headers=headers, verify=False)
#print response_get
uri = 'https://10.195.168.110/dataservice/template/config/running/11OD152130107'
response_get = s.get(uri, auth=HTTPBasicAuth('deepesh', 'deepesh4321!') , verify=False)
#print response_get
f = response_get.json()
#print f['config']
g = open('runconf1.txt', 'w')
g.write(f['config'])
g.close




#print response_get
#f = response_get.json()
#print f['data']
#for i in f['data']:
    #print 'the loss is: %s' %i['loss'], 'the latency is: %s' %i['latency'], 'the jitter is: %s' %i['jitter'], 'the remote_system_ip is: %s' %i['remote_system_ip']
#    if i['loss'] > 0:
#        print i['remote_system_ip'], i['tunnel_color'],i['loss'],i['remote_color']
#f = response_get.json()

#for i in f['data']:
#    print i['remote-system-ip'], i['mean-loss']

#response_post = s.post(uri, auth=HTTPBasicAuth('deepesh', 'deepesh4321!'), data = payload, verify=False)
#for (i,j) in zip(g,h):
#    p['devices'][0]['deviceId'] = i
#    p['devices'][0]['deviceIP'] = j
#    q = json.dumps(p)
#    response_post = s.post(urv, auth=HTTPBasicAuth('deepesh', 'deepesh4321!'), data = q, headers=headers, verify=False)
#    print response_post
