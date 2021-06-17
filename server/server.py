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

def changeDir(conn,data):
    path = os.getcwd()
    if 'main' in path:
        if path.endswith('main') and data =='cd ..':
            message = 'Bad Request!!'
            conn.sendall(message.encode())
        else:
            found =0
            destDir = data[3:]
            with os.scandir() as items:
                for item in items:
                    if destDir == item.name or destDir =='..':
                        os.chdir(destDir)
                        found =1
                        break
                if found:
                    message = 'directory changed successfully'
                    conn.sendall(message.encode())
                else:
                    message = 'Bad Request... directory not found...'
                    conn.sendall(message.encode())