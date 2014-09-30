__author__ = 'Nicolas'
import subprocess
import os.path
import platform
import tkFileDialog, Tkinter

__worlds_directories = {('Windows','7') : r'%appdata%\.minecraft\saves'}
def start_server(exe_path):
    subprocess.call(exe_path, cwd=os.path.dirname(os.path.abspath(exe_path)))

def get_worlds_directory():
    try:
        return os.path.expandvars(__worlds_directories[(platform.system(), platform.release())])
    except Exception:
        root = Tkinter.Tk()
        root.withdraw()
        return tkFileDialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')

if __name__ == '__main__':
    print get_worlds_directory()