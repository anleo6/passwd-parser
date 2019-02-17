#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
 
import sys
import argparse
import json
import collections

version = "1.0"

def createParser():
    parser = argparse.ArgumentParser(
        prog = '''passwd-parser''',
        description = '''passwd-parser 1.0 - (C) 2019 anleo6. Released under the MIT License. 
			This utility parses the UNIX /etc/passwd and /etc/groups files 
			and combines the data into a single json output. It is a toy 
			treated as a real utility program that could be run in a cron job.''')

    parser.add_argument ('-v', '--version', action ='version',
        help = 'show version of program',
        version ='%(prog)s {}'.format(version))

    parser.add_argument('-p', default ='/etc/passwd',
    	help = 'set the custom path to passwd file, by default /etc/passwd',
    	metavar = "passwd")

    parser.add_argument('-g', default ='/etc/group',
    	help = 'set the custom path to group file, by default /etc/group',
    	metavar = "group")

    return parser

def main(args = None):
    parser = createParser()
    namespace = parser.parse_args (sys.argv[1:])

# Create temporary dictionary for keep all data to moving it to json format later
    tempDict = {}

    try:
        pswd = open( "{}".format(namespace.p), "r" )

        for line in pswd:
            pFields = line.split( ":" )
            name = pFields[0]

            tempDict[name]      		= collections.OrderedDict()
            tempDict[name]["uid"]   	= pFields[2]
            tempDict[name]["full_name"] = pFields[4]
            tempDict[name]["groups"]    = []
            
            grp = open( "{}".format(namespace.g), "r" )

            for line in grp:
                gFields = line.split( ":" )
                if gFields[3] != '\n':
                    gUsers = gFields[3].rstrip().split( "," )
                    for gUser in gUsers:
                        if gUser == name:
                            tempDict[name]["groups"].append(gFields[0])
            grp.close()
        pswd.close()
    
    except:
        print("File does not exist.")
        parser.print_help()
  
    print(json.dumps(tempDict, indent = 4))

 
# Entry point 
if __name__ == "__main__":
    main()
