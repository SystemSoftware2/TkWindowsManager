from .window.manager import WindowManager
from .window.window import WindowFlags
from importlib import *
import os

def getallprograms():
    funcs = []
    directory = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/program/'
    for i in os.listdir(directory):
        if i == '__pycache__':
            continue
        funcs.append(import_module('sources.program.'+i.replace('.py', '')).run)
    return funcs

programs = getallprograms()
