#!/usr/bin/env python3

import os
import re
import shutil

source_folder='/Users/cbiphuk/Dropbox-personal/Dropbox/Camera Uploads'
dest_folder='/Volumes/Elements/BackupFromDropbox/mine'


#source_folder='/Users/cbiphuk/Dropbox-personal/Dropbox/Camera Uploads from Iryna'
#dest_folder='/Volumes/Elements/BackupFromDropbox/Iryna'

def list_folder(folder_name):
    file_list = os.listdir(source_folder)
    return file_list

def create_folder_by_filename(filename):
    folder_name = filename[0:10]
    pattern = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}.*")
    if not pattern.match(folder_name):
        print("Pattern does not match: ",folder_name )
        return None
    directory = dest_folder+'/'+folder_name
    if not os.path.exists(directory):
        os.mkdir(directory)
    return folder_name

def move_file(filename):
    folder_name = create_folder_by_filename(filename)
    if folder_name is not None:
        print("Moving file: ", filename)
        shutil.move(source_folder+'/'+filename, dest_folder+'/'+ folder_name+'/'+filename)
    else:
        print ("lazha")

def move_all_files(source_folder):
    files_list = list_folder(source_folder)
    for file in files_list:
        move_file(file)


if __name__ == '__main__':
    move_all_files(source_folder)


