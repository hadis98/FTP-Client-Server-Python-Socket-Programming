import socket
import os
import random

def ChooseCommands():
    data ="""
HELP                :show help
LIST                :list files
DWLD filePath       :download file
CD dirName          :change directory
PWD                 :show current directory
QUIT                :exit
    """
    return data

def printWorkingDir():
    path = os.getcwd()
    ans =''
    if path.endswith('main'):
        ans ='/'
        return ans
    else:
        pos = path.index('main')
        ans =path[pos+4:len(path)]
        return ans

def ListItems():
    with os.scandir() as items:
        res =''
        totalSize=0
        for item in items:
            if item.is_file():
                size = item.stat().st_size
                res += f'{item.name} \t {size}b \n'
                totalSize +=size
            elif item.is_dir():
                res += f'> {item.name} \n'
        res += f'total size: {totalSize}b \n'
        return res
