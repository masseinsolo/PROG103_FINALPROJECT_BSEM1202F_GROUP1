"""
CROP ADVISOR – ENTRY POINT
Run this file to start the application
"""

import tkinter as tk
from gui import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    login = LoginWindow(root)
    root.mainloop()