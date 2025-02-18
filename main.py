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

        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("URW Gothic", 16))
        self.s.configure("TButton", font=("URW Gothic", 16))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both",pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.pomoLabel = ttk.Label(self.tab1, default="40:00", font=("URW Gothic", 48))
        self.pomoLabel.pack(pady=20)

        self.sbLabel = ttk.Label(self.tab2, default="05:00", font=("URW Gothic", 48))
        self.sbLabel.pack(pady=20)

        self.lbLabel = ttk.Label(self.tab3, default="10:00", font=("URW Gothic", 48))
        self.lbLabel.pack(pady=20)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        self.root.mainloop()

    def start_timer(self):
        pass

    def start_timer_thread(self):
        pass

    def reset(self):
        pass

    def skip(self):
        pass

if __name__ == '__main__':
    Pomodoro()
