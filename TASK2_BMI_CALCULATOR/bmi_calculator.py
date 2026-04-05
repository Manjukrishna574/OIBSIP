
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

data=[]

def calculate_bmi():

    try:
        name=name_entry.get()
        weight=float(weight_entry.get())
        height=float(height_entry.get())

        if weight<=0 or height<=0:
            messagebox.showerror("Error","Enter valid values")
            return

        bmi=weight/(height**2)
        bmi=round(bmi,2)

        if bmi<18.5:
            category="Underweight"
            color="#eab308"

        elif bmi<25:
            category="Normal"
            color="#22c55e"

        elif bmi<30:
            category="Overweight"
            color="#f97316"

        else:
            category="Obese"
            color="#ef4444"


        result_label.config(
            text=f"Name : {name}\n\nBMI : {bmi}\nCategory : {category}",
            fg=color
        )

        data.append((name,bmi))

        file=open("bmi_data.txt","a")
        file.write(f"{name} {bmi}\n")
        file.close()

    except:
        messagebox.showerror("Error","Enter numbers only")


def show_history():

    try:
        file=open("bmi_data.txt","r")
        content=file.read()
        file.close()

        messagebox.showinfo("History",content)

    except:
        messagebox.showinfo("History","No data found")


def show_graph():

    names=[]
    bmis=[]

    for item in data:
        names.append(item[0])
        bmis.append(item[1])

    if len(bmis)==0:
        messagebox.showerror("Error","No data")
        return

    plt.plot(names,bmis,marker="o")
    plt.title("BMI Trend Analysis")
    plt.xlabel("Users")
    plt.ylabel("BMI")
    plt.show()


root=tk.Tk()
root.title("BMI Calculator")

width=450
height=500

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=(screen_width/2)-(width/2)
y=(screen_height/2)-(height/2)

root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

root.configure(bg="#0b1120")


frame=tk.Frame(
    root,
    bg="#111827",
    padx=30,
    pady=30
)

frame.place(relx=0.5,rely=0.5,anchor="center")


title=tk.Label(
    frame,
    text="BMI Calculator",
    font=("Segoe UI",22,"bold"),
    bg="#111827",
    fg="#60a5fa"
)

title.pack(pady=15)


name_entry=tk.Entry(
    frame,
    font=("Segoe UI",13),
    width=22,
    justify="center"
)

name_entry.pack(pady=8)
name_entry.insert(0,"Enter Name")


weight_entry=tk.Entry(
    frame,
    font=("Segoe UI",13),
    width=22,
    justify="center"
)

weight_entry.pack(pady=8)
weight_entry.insert(0,"Weight (kg)")


height_entry=tk.Entry(
    frame,
    font=("Segoe UI",13),
    width=22,
    justify="center"
)

height_entry.pack(pady=8)
height_entry.insert(0,"Height (m)")


btn=tk.Button(
    frame,
    text="Calculate BMI",
    font=("Segoe UI",12,"bold"),
    bg="#60a5fa",
    fg="black",
    width=18,
    pady=6,
    command=calculate_bmi
)

btn.pack(pady=15)


history_btn=tk.Button(
    frame,
    text="View History",
    font=("Segoe UI",11),
    bg="#1f2937",
    fg="white",
    width=18,
    command=show_history
)

history_btn.pack(pady=5)


graph_btn=tk.Button(
    frame,
    text="Show Graph",
    font=("Segoe UI",11),
    bg="#1f2937",
    fg="white",
    width=18,
    command=show_graph
)

graph_btn.pack(pady=5)


result_label=tk.Label(
    frame,
    text="Enter details to calculate BMI",
    font=("Segoe UI",13),
    bg="#111827",
    fg="white",
    justify="center"
)

result_label.pack(pady=20)


root.mainloop()