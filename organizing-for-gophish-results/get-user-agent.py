#!/usr/bin/env python3

import csv
import re
import subprocess
import json

def get_csv_files():
    names = []
    output = subprocess.check_output(['ls'],encoding="UTF-8").split('\n')
    for name in output:
        if name[-4:] == ".csv":
            names.append(name)
    return names

def get_details(columnname,filename):
    res = []
    with open(filename,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "payload" in row[columnname]:
                res.append(row[columnname])
    print ("[+] retrieved " + str(len(res)) + " '" + columnname + "' from " + filename)
    return res

def process_details(details_list):
    processed = []
    for deets in details_list:
        row = json.loads(deets)
        res = row['browser']['user-agent'] #user-agent
        #res = row['browser']['address'] #source ip
        processed.append(res)
        #print(deets)
        pass
    return processed


def main(columnname):
    for filename in get_csv_files():
        res = process_details(get_details(columnname,filename))
        results_filename = "res_" + columnname + "_" + filename + ".txt"
        with open(results_filename,'w') as f:
            f.write('new ' + columnname + '\n')
            for data in res:
                f.write(data)
                f.write("\n")
            f.close()
        print ("[+] new " + columnname + " results stored in " + results_filename + ".txt")
    pass

if __name__ == "__main__":
    main('details')
