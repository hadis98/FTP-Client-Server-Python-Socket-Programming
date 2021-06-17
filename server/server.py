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