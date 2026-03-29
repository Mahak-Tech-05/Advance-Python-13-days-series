import tkinter as tk

def say_hello():
    print("Hello Button clicked!")

root = tk.Tk()

btn = tk.Button(root,text = "Clicked me", command = say_hello)
btn.pack()
root.geometry("400x300")
root.mainloop()
