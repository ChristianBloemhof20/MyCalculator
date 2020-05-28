# Christian Bloemhof
# Calculator Project
#
# This calculator is to look and act similarly to the calculator built into the Macbook
# Since the mac version of tkinter does not support the changing of button colors, buttons will remain default color

from tkinter import *


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add(self="NONE"):
    first_number = e.get()
    global f_num
    global math
    global math_count
    math_count = 0
    math = "add"
    f_num = float(first_number)
    e.delete(0, END)


def button_sub(self="NONE"):
    first_number = e.get()
    global f_num
    global math
    global math_count
    math_count = 0
    math = "sub"
    f_num = float(first_number)
    e.delete(0, END)


def button_mult(self="NONE"):
    first_number = e.get()
    global f_num
    global math
    global math_count
    math_count = 0
    math = "mult"
    f_num = float(first_number)
    e.delete(0, END)


def button_div(self="NONE"):
    first_number = e.get()
    global f_num
    global math
    global math_count
    math_count = 0
    math = "div"
    f_num = float(first_number)
    e.delete(0, END)


def button_sign():
    num = e.get()
    e.delete(0, END)
    num = int(num) * -1
    e.insert(0, num)


def button_percent(self="NONE"):
    num = e.get()
    e.delete(0, END)
    num = float(num) / 100
    e.insert(0, num)


def button_equal(self="NONE"):
    second_number = e.get()
    e.delete(0, END)
    try:
        if math == "add":
            num = f_num + float(second_number)
            check_float(num)

        elif math == "sub":
            num = f_num - float(second_number)
            check_float(num)

        elif math == "mult":
            num = f_num * float(second_number)
            check_float(num)

        elif math == "div":
            try:
                num = f_num / float(second_number)
                check_float(num)
            except ZeroDivisionError:
                e.insert(0, "Not a number")

    except NameError:
        e.insert(0, second_number)


# Check float is a function that will decide whether to display a decimal point or not.
# The issue that this function solves is that before 3.0 - 2 = 1.0
#   we would much prefer 3.0 - 2 = 1

def check_float(num):
    if (num - int(num)) != 0:
        e.insert(0, float(num))
    else:
        e.insert(0, int(num))


def key_pressed(event):
    if 57 >= event.keycode >= 48:
        button_click(event.keysym)


root = Tk()
root.title("Christian Bloemhof's Calculator")

e = Entry(root)
e.grid(row=0, column=0, columnspan=4)


# Define Buttons

button_1 = Button(root, text="1", pady=15, command=lambda: button_click(1))
button_2 = Button(root, text="2", pady=15, command=lambda: button_click(2))
button_3 = Button(root, text="3", pady=15, command=lambda: button_click(3))
button_4 = Button(root, text="4", pady=15, command=lambda: button_click(4))
button_5 = Button(root, text="5", pady=15, command=lambda: button_click(5))
button_6 = Button(root, text="6", pady=15, command=lambda: button_click(6))
button_7 = Button(root, text="7", pady=15, command=lambda: button_click(7))
button_8 = Button(root, text="8", pady=15, command=lambda: button_click(8))
button_9 = Button(root, text="9", pady=15, command=lambda: button_click(9))
button_0 = Button(root, text="0", pady=15, command=lambda: button_click(0))
button_decimal = Button(root, text=".", pady=15, command=lambda: button_click("."))

button_adds    = Button(root, text="+",   pady=15, command=button_add)
button_subs    = Button(root, text="-",   pady=15, command=button_sub)
button_mults   = Button(root, text="x",   pady=15, command=button_mult)
button_divs    = Button(root, text="÷",   pady=15, command=button_div)
button_equals  = Button(root, text="=",   pady=15, command=button_equal)
button_clear   = Button(root, text="AC",  pady=15, command=button_clear)
button_sign    = Button(root, text="+/-", pady=15, command=button_sign)
button_percent = Button(root, text="%",   pady=15, command=button_percent)

# Bind the buttons to the keys on the keyboard

root.bind('<Key>', key_pressed)
root.bind('<Return>', button_equal)
root.bind('<+>', button_add)
root.bind('<minus>', button_sub)
root.bind('<*>', button_mult)
root.bind('</>', button_div)
root.bind('<%>', button_percent)

# Put the buttons on the screen in the correct order

button_0.grid(row=5, column=0, columnspan=2, ipadx=50, sticky="ew")
button_decimal.grid(row=5, column=2, ipadx=25, sticky="ew")
button_equals.grid(row=5, column=3, ipadx=20, sticky="ew")

button_1.grid(row=4, column=0, ipadx=20, sticky="ew")
button_2.grid(row=4, column=1, ipadx=20, sticky="ew")
button_3.grid(row=4, column=2, ipadx=20, sticky="ew")
button_adds.grid(row=4, column=3, ipadx=20, sticky="ew")

button_4.grid(row=3, column=0, ipadx=20, sticky="ew")
button_5.grid(row=3, column=1, ipadx=20, sticky="ew")
button_6.grid(row=3, column=2, ipadx=20, sticky="ew")
button_subs.grid(row=3, column=3, ipadx=20, sticky="ew")

button_7.grid(row=2, column=0, ipadx=20, sticky="ew")
button_8.grid(row=2, column=1, ipadx=20, sticky="ew")
button_9.grid(row=2, column=2, ipadx=20, sticky="ew")
button_mults.grid(row=2, column=3, ipadx=20, sticky="ew")

button_clear.grid(row=1, column=0, ipadx=15, sticky="ew")
button_sign.grid(row=1, column=1, ipadx=15, sticky="ew")
button_percent.grid(row=1, column=2, ipadx=20, sticky="ew")
button_divs.grid(row=1, column=3, ipadx=20, sticky="ew")

root.mainloop()