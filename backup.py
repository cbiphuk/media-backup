#!/usr/bin/env python3

import os
import re
import shutil

####
# source_folder='/Users/cbiphuk/Dropbox-personal/Dropbox/Camera Uploads'
# dest_folder='/Volumes/Elements/BackupFromDropbox/mine'


source_folder = '/Users/cbiphuk/myprojects/media-backup/source'
dest_folder = '/Users/cbiphuk/myprojects/media-backup/dest'


def list_folder(folder_name):
    file_list = os.listdir(source_folder)
    return file_list


def create_folder_by_filename(filename):
    folder_name = filename[0:10]
    pattern = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}.*")
    if not pattern.match(folder_name):
        print("Pattern does not match: ", folder_name)
        return None
    directory = os.path.join(dest_folder, folder_name)
    if not os.path.exists(directory):
        os.mkdir(directory)
    return folder_name


def move_file(filename):
    folder_name = create_folder_by_filename(filename)
    if folder_name is not None:
        # Ensure file does not exist in dest folder
        source_file = os.path.join(source_folder, filename)
        dest_file = os.path.join(dest_folder, folder_name, filename)

        if not os.path.exists(dest_file):
            print("Moving file: ", filename)
            shutil.move(source_file, dest_file)
        else:
            destfile = filename
            prefix = 0
            while True:
                name = filename.split(".")
                prefix += 1
                destfile = '.'.join(map(str, name[:-1])) \
                    + '_' + str(prefix) + '.' + name[-1]
                dest_file = os.path.join(dest_folder, folder_name, destfile)
                if not os.path.exists(dest_file):
                    break
            print("Moving renamed file: ", destfile)
            shutil.move(source_file, dest_file)
    else:
        print ("Something went wrong")


def move_all_files(source_folder):
    files_list = list_folder(source_folder)
    for file in files_list:
        move_file(file)


if __name__ == '__main__':
    move_all_files(source_folder)
