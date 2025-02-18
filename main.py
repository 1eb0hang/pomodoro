import time
import threading
# import tkinter as tk
import tkinter as tk
from tkinter import ttk, PhotoImage

class Pomodoro:
    """docstring for Pomodoro."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro Timer")
        # self.root.tk.call("wm","iconphotot", self.root._w, PhotoImage(file="file.png"))
        self.root.mainloop()

if __name__ == '__main__':
    Pomodoro()
