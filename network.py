tester@ip-10-0-1-197:~/zprov$ cat signing.py
import os
import csv
import subprocess
import time as t
import datetime as dt
import json
import argparse


import pdb
SERIAL_FILE_NAME="viptela_serial_file"
SERIAL_FILE_EXT=".viptela"

def sign_vedge_list(dummy, csv_file=None, org_name=None, output_file=None):
    ''' This function
        - the csv file as input
        - parses it, converts it into a json file of the format
            - organization
            - timestamp
            - chassis_list = [chassis:serial, ...]
        - signs the file - viptela_serial_file
        - packages the .tgz file to a .viptela extension
    '''
    base_path = os.path.dirname(os.path.abspath(__file__))
    if org_name is None :
        return [False, "org_name is not defined"]
    if csv_file is None or not os.path.isfile(csv_file):
        return [False, 'csv_file: %s is not defined or does not exist' % csv_file]

    file_info = {}
    chassis_list = []
    st = dt.datetime.fromtimestamp(t.time()).strftime('%Y-%m-%d_%H:%M:%S')
    file_info["organization"] = str(org_name)
    file_info["timestamp"] = str(st)
    with open(csv_file, 'r') as f:
        try:
            csv_reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in csv_reader:
                cols = []
                chassis = {}
                if 0 < len(row) and len(row) < 3:
                    chassis["chassis"] = str(row[0])
                    if len(row) > 1 and len(str(row[1])) > 0:
                        chassis["serial"] = str(row[1])
                    chassis_list.append(chassis)
                else:
                    return [False, 'The length of the row: %s in file %s is %s which is out of the range: [1,2]'
                            % (row, csv_file, len(row))]
        except Exception as e:
            print e
            return [False, "Failed to parse the CSV file: %s" % csv_file]

    file_info["chassis_list"] = chassis_list
    file_info = json.dumps(file_info)
    vedge_file_name = SERIAL_FILE_NAME
    with open(vedge_file_name, 'wb+') as f:
        try:
            f.write(str(file_info))
        except:
            return [False, "Failed to write to the JSON file: %s" % vedge_file_name]
    try:
        subprocess.check_output([os.path.join(base_path,"sign_zprov_file.sh"), vedge_file_name, base_path + "/", "1"])
    except Exception, e:
        err_msg = "Exception when signing the file: " + str(e) + vedge_file_name
        print(err_msg)
        return [False, err_msg]
    os.remove(vedge_file_name)
    vedge_file_name = vedge_file_name + SERIAL_FILE_EXT
    os.rename(vedge_file_name, output_file)
    return [True, 'Successfully! The signed the vEdge-list file located: %s' % output_file]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--csvfile', help='the path for the CSV vEdge-list file', type=str)
    parser.add_argument('-org', '--orgname', help='the organization name for the vEdge-list file')
    parser.add_argument('-o', '--output', help='the path for the signed vEdge-list file')
    args = parser.parse_args()
    # print "sign_vedge_list('Testbed', csv_file=%s, org_name=%s, output_file=%s)" % (args.csvfile, args.orgname, args.output)
    res = sign_vedge_list('Testbed', args.csvfile, args.orgname, args.output)
    if not res[0]:
        print "Failed! %s" % res[1]
    else:
        print res[1]tester@ip-10-0-1-197:~/