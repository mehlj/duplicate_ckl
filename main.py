import csv
import argparse
import shutil
import os
import re

parser = argparse.ArgumentParser(description='Duplicate CKL files according to a CSV list of machines.')

parser.add_argument('list',
                    metavar='list',
                    type=str,
                    help='name of the CSV file containing machine information')

parser.add_argument('ckl',
                    metavar='ckl',
                    type=str,
                    help='name of the CKL file to duplicate')

args = parser.parse_args()
input_list = args.list
input_ckl = args.ckl

file = csv.reader(open(input_list), delimiter=',')

# create output directory
try:
    os.makedirs('checklists/', exist_ok=True)
except OSError as error:
    print(error)

# start looping and duplicating CKLs
for line in file:
    # copy CKL from user-provided master copy
    new_ckl = "checklists/" + line[0] + ".ckl"
    shutil.copy2(input_ckl, new_ckl)

    # read the newly copied CKL into memory
    with open(input_ckl, 'r') as file:
        ckl_text = file.read()

    # modify data in place
    ckl_text = re.sub(r'<HOST_NAME>(.*)</HOST_NAME>', '<HOST_NAME>' + line[0] + '</HOST_NAME>', ckl_text)
    ckl_text = re.sub(r'<HOST_IP>(.*)</HOST_IP>', '<HOST_IP>' + line[1] + '</HOST_IP>', ckl_text)
    ckl_text = re.sub(r'<HOST_MAC>(.*)</HOST_MAC>', '<HOST_MAC>' + line[2] + '</HOST_MAC>', ckl_text)
    ckl_text = re.sub(r'<HOST_FQDN>(.*)</HOST_FQDN>', '<HOST_FQDN>' + line[2] + '</HOST_FQDN>', ckl_text)


    ckl_out = open(new_ckl, 'w')
    ckl_out.writelines(ckl_text)
    ckl_out.close()
