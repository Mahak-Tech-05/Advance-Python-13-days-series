import tkinter as tk

def login():
    username = user_entry.get()
    password = pass_entry.get()
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()
root.title("Login Form")

tk.Label(root , text = "Username").grid(row=0 , column = 0)
user_entry = tk.Entry(root)
user_entry.grid(row = 0 , column = 1)

tk.Label(root , text = "Password").grid(row = 1 , column = 0)
pass_entry = tk.Entry(root , show="*")#show->user entry actual data not seen at the place of it *
pass_entry.grid(row=1,column=1)

tk.Button(root , text="Login" , command=login).grid(row=2,column=1)
root.geometry("400x300")

root.mainloop()
