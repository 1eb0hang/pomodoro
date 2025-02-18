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

        self.pomoLabel = ttk.Label(self.tab1, text="40:00", font=("URW Gothic", 48))
        self.pomoLabel.pack(pady=20)

        self.sbLabel = ttk.Label(self.tab2, text="05:00", font=("URW Gothic", 48))
        self.sbLabel.pack(pady=20)

        self.lbLabel = ttk.Label(self.tab3, text="10:00", font=("URW Gothic", 48))
        self.lbLabel.pack(pady=20)

        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        self.grid = ttk.Frame(self.root)
        self.grid.pack(pady=20)

        self.btn_start = ttk.Button(self.grid, text="Stat", command=self.start_timer_thread)
        self.btn_start.grid(row=0, column=0)

        self.btn_skip = ttk.Button(self.grid, text="Skip", command=self.skip)
        self.btn_skip.grid(row=0, column=1)

        self.btn_reset = ttk.Button(self.grid, text="Reset", command=self.reset)
        self.btn_reset.grid(row=0, column=2)

        self.skipped = False
        self.stopped = False
        self.running = False

        self.root.mainloop()

    def start_timer(self):
        self.stopped = False;
        self.skipped = False;

        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 60 *40
            while full_seconds>0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomoLabel.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds-=1;

            if not self.stopped or self.skipped:
                # self.pomoLabel.config(text="")
                self.tabs.select(1)
                self.start_timer()

        elif timer_id == 2:
            full_seconds = 60 * 5
            while full_seconds>0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.sbLabel.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds-=1;

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

        elif timer_id == 3:
            full_seconds = 60*10
            while full_seconds>0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.lbLabel.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds-=1;

            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def reset(self):
        self.stopped = True
        self.skipped = False
        self.pomoLabel.config(text="40:00")
        self.sbLabel.config(text="05:00")
        self.lbLabel.config(text="10:00")
        self.running = False

    def skip(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomoLabel.config(text="40:00")

        elif current_tab == 1:
            self.sbLabel.config(text="05:00")

        elif current_tab == 2:
            self.lbLabel.config(text="10:00")

        self.stopped = True
        self.skipped = True


if __name__ == '__main__':
    Pomodoro()
