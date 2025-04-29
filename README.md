# Description
Toy window manager in the style of Windows 3.x on Tkinter

<img src="https://habrastorage.org/webt/ci/8k/3r/ci8k3rlufs8epkjfhvpshc9unm0.png" />

## Features

- Create new windows
- Drag and resize windows
- Minimize, maximize and close windows
- Create child windows inside other windows
- Context menus for windows
- Window focus

## Programs:

**Warning!** These programs are only demo versions to demonstrate the manager's work and do not have useful functionality.

- **Terminal** - toy command line
- **Notepad** - toy notepad
- **Calculator** - calculator with support for basic operations

You can write your own program, see the instructions below

# Installation

The program requires the pillow library to work. You can install it with the command `pip install pillow`

# Usage

Run `python main.py` to start

# Creating your own programs

To add your own program to the manager, create a file of your program in the `sources\program` directory, for example `test.py`.
Then you can write your code. But you should keep in mind that the main class of your program should inherit from `tkinter.Frame`

Example:
```
import tkinter as tk


class Test(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_area = tk.Text(
            self, wrap=tk.WORD, width=40, height=10, font=("Fixedsys", 12))
        self.text_area.pack(fill="both", expand=True)

def run(app):
    app.create_window(title="Test", content=Test,
                      size=(800, 50, 200, 300), flags=WindowFlags.WN_DRAGABLE)
```

There are:
 - `title` - this is the title of your window
 - `content` - the object of your program
 - `size` - coordinates and size of the window
 - `flags` - window flags

A little about flags. 'WN' means 'Window Not', so 'WN_DRAGABLE' means 'Window Not Dragable', 'WN_RESIZABLE' means 'Window Not Resizable', and so on. There are 3 of them:
 - WN_CONTROLS 
 - WN_DRAGABLE
 - WN_RESIZABLE
