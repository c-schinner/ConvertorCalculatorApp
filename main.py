import tkinter
from tkinter import *

# More conversion types can be added easily
# make adjustment to the button function (add more elif statements with the correct conversions)
# add new radio buttons and functions to change the labels

window = tkinter.Tk()
window.title("Unit Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

convert_from_label = tkinter.Label(window, text=" ", font=("Italic", 10, "bold"))
convert_to_label = tkinter.Label(window, text=" ", font=("Italic", 10, "bold"))
is_equal_label = tkinter.Label(window, text="is equal to", font=("Italic", 10, "bold"))
finished_conversion = tkinter.Label(window, text="0", font=("Italic", 10, "bold"))
finished_conversion.config(padx=30, pady=30)

convert_from_label.grid(column=2, row=0)
convert_to_label.grid(column=2, row=1)
is_equal_label.grid(column=0, row=1)
finished_conversion.grid(column=1, row=1)


def button_convert():
    if convert_change.get() == "mile to km":
        convert_data = float(user_input.get())
        km = round(convert_data * 1.609, 2)
        finished_conversion.config(text=km)

    elif convert_change.get() == "inch to cm":
        convert_data = float(user_input.get())
        cm = round(convert_data * 2.54, 2)
        finished_conversion.config(text=cm)

    elif convert_change.get() == "feet to meter":
        convert_data = float(user_input.get())
        meter = round(convert_data / 3.281, 2)
        finished_conversion.config(text=meter)

    elif convert_change.get() == "oz to cup":
        convert_data = float(user_input.get())
        cup = round(convert_data / 8, 2)
        finished_conversion.config(text=cup)

    elif convert_change.get() == "f to c":
        convert_data = float(user_input.get())
        c = round((convert_data - 32) * 5 / 9, 2)
        finished_conversion.config(text=c)


button = tkinter.Button(window, text="calculate", font=("Italic", 10, "bold"), command=button_convert)
button.grid(column=1, row=2)

user_input = tkinter.Entry(width=5, font=("Italic", 10, "bold"))
user_input.grid(column=1, row=0)


def change_mile_km():
    convert_from_label.config(text="Miles")
    convert_to_label.config(text="Km")


def change_inch_cm():
    convert_from_label.config(text="Inch")
    convert_to_label.config(text="Cm")


def change_feet_meter():
    convert_from_label.config(text="Feet")
    convert_to_label.config(text="Meters")


def change_oz_cup():
    convert_from_label.config(text="Ounce")
    convert_to_label.config(text="Cups")


def change_f_c():
    convert_from_label.config(text="F")
    convert_to_label.config(text="C")


convert_change = tkinter.StringVar()

mile_km = Radiobutton(text="Mile to Km", value="mile to km", variable=convert_change, command=change_mile_km)
inch_cm = Radiobutton(text="Inch to Cm", value="inch to cm", variable=convert_change, command=change_inch_cm)
feet_meter = Radiobutton(text="Feet to Meter", value="feet to meter", variable=convert_change,
                         command=change_feet_meter)
oz_cup = Radiobutton(text="Ounces to Cups", value="oz to cup", variable=convert_change, command=change_oz_cup)
f_c = Radiobutton(text="F to C", value="f to c", variable=convert_change, command=change_f_c)

mile_km.grid(column=1, row=4)
mile_km.config(padx=2, pady=5)

inch_cm.grid(column=1, row=5)
inch_cm.config(padx=2, pady=5)

feet_meter.grid(column=1, row=6)
feet_meter.config(padx=2, pady=5)

oz_cup.grid(column=1, row=7)
oz_cup.config(padx=2, pady=5)

f_c.grid(column=1, row=8)
f_c.config(padx=2, pady=5)

window.mainloop()
