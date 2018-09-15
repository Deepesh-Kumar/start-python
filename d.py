import json
import requests
import itertools
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s = requests.session()




uri = 'https://10.195.168.110/dataservice/template/config/running/11OD152130107'
response_get = s.get(uri, auth=HTTPBasicAuth('deepesh', 'deepesh4321!') , verify=False)
#print response_get
f = response_get.json()
#print f['config']
g = open('runconf1.txt', 'w')
g.write(f['config'])
g.close



