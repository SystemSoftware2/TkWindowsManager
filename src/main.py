import tkinter as tk
from sources.window.manager import WindowManager
from sources.window.window import WindowFlags
from sources.program.notepad import Notepad
from sources.program.terminal import Terminal
from sources.program.calc import Calculator


def main():
    root = tk.Tk()

    app = WindowManager(root) 

    app.create_window(title="Notepad", content=Notepad,
                      size=(800, 50, 200, 300), flags=WindowFlags.WN_DRAGABLE)
    app.create_child(app.windows[0], title="Notepad", content=Notepad,)
    app.create_window(title="Terminal", content=Terminal,
                      size=(275, 50, 500, 300), flags=WindowFlags.WN_CONTROLS)
    app.create_window(title="Calculator", content=Calculator,
                      size=(50, 200, 500, 300), flags=WindowFlags.WN_RESIZABLE)

    root.mainloop()


if __name__ == "__main__":
    main()
