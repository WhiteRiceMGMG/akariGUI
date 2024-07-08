import tkinter as tk


root = tk.Tk()
root.title("notify system")
root.geometry("300x200")

frame = tk.Frame(root)
frame.grid(column=0, row=0)

label = tk.Label(frame, text="enter notification")
entry = tk.Entry(frame)
button = tk.Button(frame, text="SEND")

label.grid(row=0, column=0)
entry.grid(row=1, column=0)
button.grid(row=2, column=0)

root.mainloop()