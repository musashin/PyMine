__author__ = 'Nicolas'
import subprocess
import os.path

def start_server(exe_path):
    subprocess.call(exe_path, cwd=os.path.dirname(os.path.abspath(exe_path)))