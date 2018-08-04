
import time
import requests
from requests.auth import HTTPBasicAuth

page = ''
while page == '':
    try:
        page = requests.get('https://34.203.116.253:8443/j_security_check', auth=HTTPBasicAuth('admin', 'admin'), verify=False)
        page.status_code
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(1)
        print("Was a nice sleep, now let me continue...")
        continue






			



