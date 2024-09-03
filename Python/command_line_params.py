#!/usr/bin/python

from argparse import ArgumentParser

def print_usage():
    print"Usage: command_line_params.py - d yyyy-mm-dd, -c y/n"

parser = ArgumentParser()

parser.add_argument("-d", "--date", dest="start_date", help="Specify starting date yyyy-mm-dd")
parser.add_argument("-c", "--check_for_duplicates", dest="check_for_duplicates", help="Specify whether or not to check for duplicate record in database: y/n")

args = parser.parse_args()

params = vars(args)
param_count = len(params)

if param_count != 2:
    print_usage()
    exit()


date = params['start_date']
check_for_duplicates = params["check_for_duplicates"]

print date
print check_for_duplicates


