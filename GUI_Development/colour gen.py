import tkinter as tk
import random

def random_color():
    # generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#%02x%02x%02x" % (r, g, b)

def change_color():
    color = random_color()
    label.config(bg=color)
    # update the label text with the hex code of the color
    label.config(text=color)

def copy_to_clipboard():
    # copy the text to the clipboard
    root.clipboard_append(label['text'])

# create the main window
root = tk.Tk()
root.title("Random Color Generator")

# make the window not resizeable
root.resizable(False, False)
root.geometry("250x250")

# create a label
label = tk.Label(root, text="Click Here", font=("Helvetica", 16))
label.pack(pady=20)

# create a button to generate a new color
button_generate = tk.Button(root, text="Generate", font=("Helvetica", 16), command=change_color)
button_generate.pack(pady=20)

# create a button to copy the text to the clipboard
button_copy = tk.Button(root, text="Copy", font=("Helvetica", 16), command=copy_to_clipboard)
button_copy.pack(pady=20)

# run the main loop
root.mainloop()

