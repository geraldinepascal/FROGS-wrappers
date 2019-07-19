# -*- coding: utf-8 -*-
from galaxy.util.json import from_json_string, to_json_string
import os, sys, argparse, time, json

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--database")
    parser.add_argument("-r","--resource")
    parser.add_argument("-o","--output")
    args = parser.parse_args()
    return args

def frogs_sources(resource)
    if resource=="ITS":
        print("ok")
    elif resource=="silva128":
        print("ok")
    elif resource=="silva132":
        print("ok")

#def HVL_sources(resource):

#def phiX_sources(resource):

def main():

    #get args from command line
    args = get_args()

    # Extract json file params
    data_manager_dict = {}
    filename = args.output
    params = from_json_string(open(filename).read())
    target_directory = params[ 'output_data' ][0]['extra_files_path']
    os.mkdir(target_directory)

    if args.database=="frogs_db_data":
        frogs_sources(args.resource)
    elif args.database=="HVL_db_data":
        HVL_sources(args.resource)
    elif args.database=="phiX_db_data":
        phiX_sources(args.resource)

if __name__ == "__main__":
    main()
