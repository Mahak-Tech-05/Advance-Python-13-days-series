import tkinter as tk

def show_text():
    print(entry.get())#.get-> it is a function using which we get data 

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root , text = "Submit", command=show_text)
btn.pack()

root.geometry("400x300")

root.mainloop()
