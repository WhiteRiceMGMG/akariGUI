import tkinter as tk


root = tk.Tk()
root.title("notify system")
root.geometry("300x200")


label_token = tk.Label(text="enter your token")
entry_token = tk.Entry(width=26)
label_notify = tk.Label(text="enter notification")
entry_text = tk.Text(width=30,height=5)
button = tk.Button(text="SEND",width=10)

label_token.place(x=55,y=15)
entry_token.place(x=55,y=40)
label_notify.place(x=55,y=65)
entry_text.place(x=55,y=87)
button.place(x=105,y=165)


root.mainloop()