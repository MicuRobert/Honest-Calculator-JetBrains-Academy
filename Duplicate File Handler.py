import os
from sys import argv
import hashlib


def init_update_dict():
    if size in dictionary.keys():
        dictionary[size] = dictionary[size] + '\n' + path
    else:
        dictionary[size] = path


def print_sorted():
    sort = sorted(dictionary.keys(), reverse=sort_option)
    for k in sort:
        print(f'{k} bytes', dictionary[k], sep='\n')
        print()

#argv.append('module\root_folder')
if len(argv) <= 1:
    print("Directory is not specified")
else:
    form = '.' + input('Enter file format: ').strip()
    print('Size sorting options:\n', '1. Descending\n', '2. Ascending\n')
    while True:
        sorting = int(input('Enter a sorting option: '))
        print()
        if sorting == 1 or sorting == 2:
            break
        else:
            print('Wrong option')
    dictionary = {}
    for root, directory, files in os.walk(argv[1]):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            if form == '.':
                init_update_dict()
            if os.path.splitext(path)[1] == form:
                init_update_dict()
    sort_option = False
    if sorting == 1:
        sort_option = True
    print_sorted()

while True:
    check_duplicates = input('Check for duplicates? ')
    print()
    if check_duplicates in ['yes', 'no']:
        break

if check_duplicates == 'yes':
    count = 1
    dict_duplicates = {}
    for k in sorted(dictionary.keys(), reverse=sort_option):
        print(f'{k} bytes')
        paths = dictionary[k].split('\n')
        dictionary_hashes = {}
        for path in paths:
            hash = hashlib.md5()
            with open(path, 'rb') as file:
                for line in file:
                    hash.update(line)
            digest = hash.hexdigest()
            if digest in dictionary_hashes.keys():
                dictionary_hashes[digest] = dictionary_hashes[digest] + '\n' + path
            else:
                dictionary_hashes[digest] = path
        for k in dictionary_hashes.keys():
            if len(dictionary_hashes[k].split('\n')) > 1:
                print(f'Hash: {k}')
                for x in dictionary_hashes[k].split('\n'):
                    print(f'{count}. {x}')
                    dict_duplicates[count] = x
                    count +=1
                print()

while True:
    delete_duplicates = input('Delete files? ')
    if delete_duplicates in ['yes', 'no']:
        print()
        break
    print('Wrong option')

while True:
    stop = True
    if delete_duplicates == 'yes':
        files_to_delete = input('Enter file numbers to delete: ')
        if files_to_delete != '':
            for file in files_to_delete.split(' '):
                if file.isalpha():
                    stop = False
        else:
            stop = False
    if stop:
        freed = 0
        if len(dict_duplicates.keys()) > 1:
            for file in files_to_delete.split(' '):
                freed += os.path.getsize(dict_duplicates[int(file)])
                os.remove(dict_duplicates[int(file)])
        print(f'Total freed up space: {freed} bytes')
        break
    else:
        print('Wrong format')
