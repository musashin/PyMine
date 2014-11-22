__author__ = 'Nicolas'
import subprocess
import os.path
import platform
import tkFileDialog, Tkinter
import localisation
from os import listdir
from os.path import isdir, join
import server_prop
import conf

__worlds_directories = {('Windows', '7'): r'%appdata%\.minecraft\saves'}
def start_server(exe_path):
    subprocess.call(exe_path, cwd=os.path.dirname(os.path.abspath(exe_path)))

def get_worlds_directory():
    try:
        return os.path.expandvars(__worlds_directories[(platform.system(), platform.release())])
    except Exception:
        root = Tkinter.Tk()
        root.withdraw()
        return tkFileDialog.askdirectory(parent=root, initialdir="/", title=localisation.get_dialog('worldFolderSelection'))

def get_world_names():
    return [d for d in listdir(get_worlds_directory()) if isdir(join(get_worlds_directory(), d))]

def set_world(name):
    print os.path.join(os.path.dirname(conf.server_full_path), 'server.properties')
    prop = server_prop.ServerProp(os.path.join(os.path.dirname(conf.server_full_path), 'server.properties'))
    prop.load()
    worldPath = '\'' + os.path.relpath(os.path.join(get_worlds_directory(), name), conf.server_full_path)+ '\''
    worldPath2 = ''
    for letter in worldPath:
        if letter == '\\':
            worldPath2 += '\\\\'
        else:
            worldPath2 += letter
    prop.set('level-name', worldPath2)
    prop.save()

if __name__ == '__main__':
    print get_world_names()