import tkinter as tk
from tkinter import scrolledtext
from .. import *

class Notepad(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=10, font=("Fixedsys", 12))
        self.text_area.pack(fill="both", expand=True)

def run(app):
    app.create_window(title="Notepad", content=Notepad,
                      size=(800, 50, 200, 300), flags=WindowFlags.WN_DRAGABLE)
