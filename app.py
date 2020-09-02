import tkinter as tk
from game import Game

root = tk.Tk()
root.title("ROCK, PAPER & SCISSORS")
root.configure(bg="#152a38")
app = Game(root)
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
root.mainloop()