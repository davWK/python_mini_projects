#!/usr/bin/env python3

"""
This script renames all files with a specified extension in a given directory with a   
specified prefix and a number sequence. It is useful for bulk renaming files in an 
automated fashion. 
"""

import os 

def main():

    path = str(input("Input the directory absolute path: "))
    if not path.endswith('/'):
        path += '/'
    ext = str(input(" Input files extension: "))
    if not ext.startswith('.'):
        ext = "." + ext

    word = str(input('Input the desired prefix for files name: '))

    # Check if there are any files with the specified extension
    file_exists = False
    while not file_exists:
        for file in os.listdir(path):
            if file.endswith(ext):
                file_exists = True
                break
        if not file_exists:
            print(f"No files with extension {ext} were found in the directory {path}.")
            ext = str(input("Please enter a different extension: "))
            if not ext.startswith('.'):
                ext = "." + ext

    #rename files
    i = 0
    for file in os.listdir(path) :
        initial_name = path + file
        final_name = word + '-' + str(i) + ext
        final_name = path + final_name
        os.rename(initial_name, final_name)
        i += 1

if __name__ == '__main__':
    main()
