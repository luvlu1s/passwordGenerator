import tkinter as tk
from tkinter import ttk
import random

def generatePassword():
    try:
        length = int(length_entry.get())
        if length < 5:
            entryE1.delete(0, tk.END)
            entryE1.insert(0, "Increase the length")
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
            entryE1.delete(0, tk.END)
            entryE1.insert(0, password)
    except ValueError:
        entryE1.delete(0, tk.END)
        entryE1.insert(0, "Invalid length")

root = tk.Tk()
root.geometry('460x350')
root.resizable(False, False)
root.title('Password Generator')

frame = ttk.Frame(root, padding=10)
frame.pack()

labelL1 = ttk.Label(frame, text="Password:")
labelL1.grid(row=0, column=0)

entryE1 = ttk.Entry(frame)
entryE1.grid(row=0, column=1)

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=1, column=0)

length_entry = ttk.Entry(frame)
length_entry.grid(row=1, column=1)

generate_button = ttk.Button(frame, text='Generate', command=generatePassword)
generate_button.grid(row=2, column=0, columnspan=2)

close_button = ttk.Button(frame, text="Close app", command=root.destroy)
close_button.grid(row=3, column=0, columnspan=2)

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+/.;:'

root.mainloop()
