import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
tk.Label(root , text = "Name").grid(row = 0 , column = 0)#.grid-> showing the data in table fomat
tk.Entry(root).grid(row = 0, column = 1)


root.mainloop()
