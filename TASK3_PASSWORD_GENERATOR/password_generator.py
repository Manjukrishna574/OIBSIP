import secrets
import string
from tkinter import *
from tkinter import messagebox

# PASSWORD GENERATOR

def generate_password():

    try:
        length=int(length_box.get())
    except:
        length=8

    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    numbers=string.digits
    symbols=string.punctuation

    all_chars=""

    if lower_var.get():
        all_chars+=lower

    if upper_var.get():
        all_chars+=upper

    if num_var.get():
        all_chars+=numbers

    if sym_var.get():
        all_chars+=symbols

    if all_chars=="":
        messagebox.showerror(
        "Error",
        "Select at least one option"
        )
        return

    password="".join(

    secrets.choice(all_chars)

    for i in range(length)

    )

    password_box.delete(0,END)

    password_box.insert(0,password)

    check_strength(password)

# PASSWORD STRENGTH

def check_strength(password):

    strength=0

    if len(password)>=8:
        strength+=1

    if any(c.isupper() for c in password):
        strength+=1

    if any(c.islower() for c in password):
        strength+=1

    if any(c.isdigit() for c in password):
        strength+=1

    if any(c in string.punctuation for c in password):
        strength+=1

    if strength<=2:

        strength_label.config(
        text="Weak Password",
        fg="#ff4d4d"
        )

    elif strength==3:

        strength_label.config(
        text="Medium Password",
        fg="#ffaa00"
        )

    else:

        strength_label.config(
        text="Strong Password",
        fg="#00cc66"
        )

# COPY PASSWORD

def copy_password():

    pwd=password_box.get()

    if pwd=="":

        return

    root.clipboard_clear()

    root.clipboard_append(pwd)

    messagebox.showinfo(
    "Copied",
    "Password copied to clipboard"
    )

# GUI

root=Tk()

root.title("Advanced Password Generator")

root.geometry("450x520")

root.configure(bg="#121212")

title=Label(

root,

text="Advanced Password Generator",

font=("Arial",18,"bold"),

bg="#121212",

fg="white"

)

title.pack(pady=15)

# LENGTH

Label(

root,

text="Password Length",

font=("Arial",14),

bg="#121212",

fg="white"

).pack()

length_box=Spinbox(

root,

from_=6,

to=40,

font=("Arial",13),

width=8

)

length_box.pack(pady=10)

# OPTIONS FRAME

options_frame=Frame(

root,

bg="#121212"

)

options_frame.pack(pady=10)

lower_var=IntVar(value=1)

upper_var=IntVar(value=1)

num_var=IntVar(value=1)

sym_var=IntVar(value=1)

Checkbutton(

options_frame,

text="Lowercase Letters",

variable=lower_var,

font=("Arial",13),

bg="#121212",

fg="white",

selectcolor="#2b2b2b",

activebackground="#121212"

).pack(anchor="w",pady=3)

Checkbutton(

options_frame,

text="Uppercase Letters",

variable=upper_var,

font=("Arial",13),

bg="#121212",

fg="white",

selectcolor="#2b2b2b",

activebackground="#121212"

).pack(anchor="w",pady=3)

Checkbutton(

options_frame,

text="Numbers",

variable=num_var,

font=("Arial",13),

bg="#121212",

fg="white",

selectcolor="#2b2b2b",

activebackground="#121212"

).pack(anchor="w",pady=3)

Checkbutton(

options_frame,

text="Symbols",

variable=sym_var,

font=("Arial",13),

bg="#121212",

fg="white",

selectcolor="#2b2b2b",

activebackground="#121212"

).pack(anchor="w",pady=3)

# GENERATE BUTTON

Button(

root,

text="Generate Password",

font=("Arial",14,"bold"),

bg="#00aa88",

fg="white",

width=18,

command=generate_password

).pack(pady=15)

# PASSWORD BOX

password_box=Entry(

root,

font=("Arial",16),

width=24,

justify="center"

)

password_box.pack(pady=10)

# COPY BUTTON

Button(

root,

text="Copy Password",

font=("Arial",13),

bg="#2979ff",

fg="white",

width=15,

command=copy_password

).pack(pady=10)

# STRENGTH LABEL

strength_label=Label(

root,

text="Password Strength",

font=("Arial",14,"bold"),

bg="#121212"

)

strength_label.pack(pady=15)

root.mainloop()