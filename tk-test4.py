import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
messagebox.showinfo('showinfo', 'completed!')

messagebox.showerror('showerror', 'error')