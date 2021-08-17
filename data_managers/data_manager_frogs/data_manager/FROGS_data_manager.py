#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import json
import os
import argparse
# import sys
import tarfile
import urllib
import time

import requests

from galaxy.util.json import from_json_string, to_json_string

# GALAXY_database=~/galaxy/galaxy-20.09/database
# FROGS_data_manager.py --database=frogs_db_data --all_dbs=false \
# --date=0 --amplicons=16S --bases=SILVA --filters=Pintail100 \
# --only_last_versions=true \
# --tool_data=/home/maria/galaxy/galaxy-20.09/tool-data \
# --output $GALAXY_database/objects/e/7/7/dataset_e7766c39-8f36-450c-adf5-3e4ee8d5c562.dat


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--database")
    parser.add_argument("--all_dbs")
    parser.add_argument("--date")
    parser.add_argument("--amplicons")
    parser.add_argument("--bases")
    parser.add_argument("--filters")
    parser.add_argument("--only_last_versions")
    parser.add_argument("--tool_data")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()

    return args


def _add_data_table_entry(data_manager_dict, data_table_entry, data_table):
    data_manager_dict['data_tables'] = data_manager_dict.get('data_tables', {})
    data_manager_dict['data_tables'][data_table] = data_manager_dict['data_tables'].get(data_table, [])
    data_manager_dict['data_tables'][data_table].append(data_table_entry)
    return data_manager_dict


def keep_only_last_version(db_index):
    db_dict = dict()
    for line in db_index:
        db_type = "_".join(line[1:4]) if line[3] != "" else "_".join(line[1:3])
        if db_type not in db_dict:
            db_dict[db_type] = line
    return list(db_dict.values())


def frogs_sources(data_manager_dict, target_directory):

    # variables
    amplicons_list = []
    bases_list = []
    filters_list = []
    if args.all_dbs == "false":
        amplicons_list = [amplicon.lower().strip() for amplicon in args.amplicons.split(",") if amplicon != ""]
        bases_list = [base.lower().strip() for base in args.bases.split(",") if base != ""]
        filters_list = [filter.lower().strip() for filter in args.filters.split(",") if filter != ""]
        bottom_date = int(args.date)
    tool_data_path = args.tool_data

    # get frogs database index
    frogs_db_index_link = "http://genoweb.toulouse.inra.fr/frogs_databanks/assignation/FROGS_databases.tsv"
    with requests.Session() as s:
        download = s.get(frogs_db_index_link)
        decoded_content = download.content.decode('utf-8')
        db_index = decoded_content.splitlines()
        db_index = [line.split("\t") for line in db_index[1:]]
        db_index = [[line[0], line[1].lower(), line[2].lower(), line[3].lower()] + line[4:] for line in db_index]

    # filter databases
    if args.all_dbs == "false":
        # filter by amplicons
        if len(amplicons_list) != 0:
            db_index = [line for line in db_index if any([amplicon in amplicons_list for amplicon in line[1].split(',')])]
        # filter by base
        if len(bases_list) != 0:
            db_index = [line for line in db_index if line[2] in bases_list]
        # filter by filters
        if len(filters_list) != 0:
            db_index = [line for line in db_index if line[3] in filters_list]
        # filter by date
        if bottom_date != 0:
            db_index = [line for line in db_index if int(line[0]) >= bottom_date]
    if args.only_last_versions == "true":
        # keep only last version
        db_index = keep_only_last_version(db_index)

    # get frogs dbs
    os.chdir(target_directory)
    dir_name = "frogs_db_"+time.strftime("%Y%m%d")
    os.mkdir(dir_name)
    dbs = set([])
    for line in db_index:
        value = line[5]
        name = value.replace("_", " ") if "_" not in line[4] else value.replace(line[4], "").replace("_", " ") + line[4]
        link = line[6]
        name_dir = "".join([line[6].replace(".tar.gz", "").split("/")[-1]])
        file_path = tool_data_path+"/frogs_db/"+name_dir
        if not os.path.exists(file_path):   # if the file is not already in frogs_db directory

            # download frogs db
            dl_file = urllib.request.URLopener()
            dl_file.retrieve(link, "tmp.tar.gz")

            # unzip frogs db
            with tarfile.open("tmp.tar.gz") as tar:
                tar.extractall(dir_name)
                tar.close()
                os.remove('tmp.tar.gz')

            # get fasta file path
            tmp = set(os.listdir(dir_name))
            new_db = dir_name+"/"+"".join(tmp.difference(dbs))
            files = os.listdir(new_db)
            fasta = "".join([file for file in files if file.endswith('.fasta')])
            path = new_db+'/'+fasta
            dbs = os.listdir(dir_name)
            # release = value + "_" + time.strftime("%Y-%m-%d")
            # date = time.strftime("%Y%m%d")
            path = os.path.join(target_directory, path)

            data_table_entry = dict(name=name, value=value, path=path)
            _add_data_table_entry(data_manager_dict, data_table_entry, "frogs_db")

# def HVL_sources(data_manager_dict,target_directory):
#     HVL_dir = "http://genoweb.toulouse.inra.fr/frogs_databanks/HVL/ITS/UNITE_s_7.1_20112016"
#     os.chdir(target_directory)
#     for link in [HVL_dir + "/Unite_s_7.1_20112016_ITS1.fasta",HVL_dir + "/Unite_s_7.1_20112016_ITS2.fasta"]:
#         file_name=link.split("/")[-1].replace('.fasta',"_"+time.strftime("%Y-%m-%d")+".fasta")
#         dl_file = urllib.URLopener()
#         dl_file.retrieve(link,file_name)

#         #get fasta file path
#         path = os.path.join(target_directory,file_name)
#         if link.endswith('ITS1.fasta'):
#             name = "UNITE 7.1 ITS1 " + time.strftime("%Y-%m-%d")
#         elif link.endswith('ITS2.fasta'):
#             name = "UNITE 7.1 ITS2 " + time.strftime("%Y-%m-%d")
#         value=file_name.replace('.fasta','')

#         data_table_entry = dict(name = name, value = value, path=path)
#         _add_data_table_entry(data_manager_dict, data_table_entry, "frogs_HVL_db")


def main():

    # get args from command line
    global args
    args = get_args()

    # Extract json file params
    data_manager_dict = {}
    filename = args.output
    params = from_json_string(open(filename).read())
    target_directory = params['output_data'][0]['extra_files_path']
    os.mkdir(target_directory)

    # if args.database=="frogs_db_data":
    frogs_sources(data_manager_dict, target_directory)
    # elif args.database=="HVL_db_data":
    #     HVL_sources(data_manager_dict,target_directory)

    # save info to json file
    open(filename, 'wt').write(to_json_string(data_manager_dict))


if __name__ == "__main__":
    main()
