# -*- coding: utf-8 -*-
from galaxy.util.json import from_json_string, to_json_string
import os, sys, argparse, time, json, requests, urllib, tarfile

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--database")
    parser.add_argument("-r","--resource")
    parser.add_argument("-o","--output")
    args = parser.parse_args()
    return args

def _add_data_table_entry(data_manager_dict, data_table_entry,data_table):
    data_manager_dict['data_tables'] = data_manager_dict.get('data_tables', {})
    data_manager_dict['data_tables'][data_table] = data_manager_dict['data_tables'].get(data_table, [])
    data_manager_dict['data_tables'][data_table].append(data_table_entry)
    return data_manager_dict

def frogs_sources(data_manager_dict,target_directory):

    #get frogs database index
    frogs_db_index_link="http://genoweb.toulouse.inra.fr/frogs_databanks/assignation/FROGS_databases.tsv"
    with requests.Session() as s:
        download = s.get(frogs_db_index_link)
        decoded_content = download.content.decode('utf-8')
        db_index = download.content.splitlines()    
        db_index = [line.split("\t") for line in db_index[1:]]
        db_index = [line[:4]+[line[1]+"_"+line[2]+"_"+line[3]]+[line[4]] for line in db_index]  #add column name

    #get frogs dbs
    os.chdir(target_directory)
    dir_name="frogs_db_"+time.strftime("%Y%m%d")
    os.mkdir(dir_name)
    dbs=set([])
    for line in db_index:
        value=line[4]
        name=value.replace("_"," ")
        link=line[5]

        #download frogs db
        dl_file = urllib.URLopener()
        dl_file.retrieve(link, "tmp.tar.gz")
        
        #unzip frogs db
        with tarfile.open("tmp.tar.gz") as tar:
            tar.extractall(dir_name)
            tar.close()
            os.remove('tmp.tar.gz')
        
        #get fasta file path
        tmp = set(os.listdir(dir_name))
        new_db = dir_name+"/"+"".join(tmp.difference(dbs))
        files = os.listdir(new_db)
        fasta = "".join([file for file in files if file.endswith('.fasta')])
        path = new_db+'/'+fasta
        dbs = os.listdir(dir_name)
        release = value+"_"+time.strftime("%Y-%m-%d")
        date=time.strftime("%Y%m%d")
        path = os.path.join(target_directory,path)

        data_table_entry = dict(name = name, value = value, path=path)
        _add_data_table_entry(data_manager_dict, data_table_entry, "frogs_db")

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
        frogs_sources(data_manager_dict,target_directory)
    elif args.database=="HVL_db_data":
        HVL_sources(args.resource)
    elif args.database=="phiX_db_data":
        phiX_sources(args.resource)

    #save info to json file
    open(filename, 'wb').write(to_json_string(data_manager_dict))

if __name__ == "__main__":
    main()
