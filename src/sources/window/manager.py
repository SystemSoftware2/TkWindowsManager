import tkinter as tk
import os
from .window import Window


class WindowManager:
    """Main window manager class that handles the desktop environment.

    Provides the main application window and manages creation of child windows.
    """

    def __init__(self, root):
        """Initialize the window manager.

        Args:
            root: The root Tkinter window
        """
        self.root = root
        self.root.title("Window Manager")
        self.root.attributes("-fullscreen", True)
        self.windows = []

        if os.name == "nt":
            self.root.iconbitmap("./assets/icon.ico")
            self.root.config(cursor="@./assets/cursor_a.cur")

        self.main_frame = tk.Frame(self.root, bg="#29A97E")
        self.main_frame.pack(fill="both", expand=True)

    def create_window(self, title="Window", content=None, size=(50, 50, 210, 200), flags=0):
        """
        Create a new top-level window

        Args:
            title: The title of the window
            content: The content widget to be placed inside the window
            size: A tuple of (x, y, width, height) for the window's initial position and size
            flags: Bitmap flags for window options

        Returns:
            Window: The newly created window
        """

        window = Window(self.main_frame, title, content, size, flags)
        self.windows.append(window)

        return window

    def create_child(self, parent: Window, title="Window", content=None, size=(50, 50, 210, 200), flags=0):
        """
        Create a new child window inside the given parent window

        Args:
            parent: The parent Window instance

        Returns:
            Window: The newly created child window
        """

        child = parent.create_child(
            title, content=content, size=size, flags=flags)
        self.windows.append(child)

        return child
