import tkinter as tk
from sources import *
from importlib import *
import os

def getallprograms():
    funcs = []
    directory = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/sources/program/'
    for i in os.listdir(directory):
        if i == '__pycache__':
            continue
        funcs.append(import_module('sources.program.'+i.replace('.py', '')).run)
    return funcs

programs = getallprograms()

def main():
    root = tk.Tk()

    app = WindowManager(root) 

    for i in programs:
        i(app)

    root.mainloop()


if __name__ == "__main__":
    main()
