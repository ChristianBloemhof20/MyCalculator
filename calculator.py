# Christian Bloemhof
# Calculator Project
#
# This calculator is to look and act similarly to the calculator built into the Macbook
# Since the mac version of tkinter does not support the changing of button colors, buttons will remain default color

# API key: 9edec1cfeeedb9c0d42474a34ace0b48
# API Information: api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={your api key}

from math import *
from random import random
from tkinter import *
import requests
import json

second = 0
memory = 0


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

        elif math == "expo":
            num = pow(f_num, float(second_number))
            check_float(num)

        elif math == "root":
            num = pow(f_num, 1/float(second_number))
            check_float(num)

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


def button_fullsize():
    root.geometry("700x330")


def button_smallsize():
    root.geometry("243x330")


def button_smile():
    e.delete(0, END)
    e.insert(0, 43770)


def button_ms():
    global memory
    memory = e.get()


def button_mc():
    global memory
    memory = 0
    e.delete(0, END)
    e.insert(0, 0)


def button_mPlus():
    global memory
    memory = float(memory) + float(e.get())
    e.delete(0, END)
    check_float(memory)


def button_mMinus():
    global memory
    memory = float(memory) - float(e.get())
    e.delete(0, END)
    check_float(memory)


def button_mr():
    e.delete(0, END)
    check_float(float(memory))


def button_squared():
    num = e.get()
    e.delete(0, END)
    num = float(num)**2
    check_float(num)


def button_cubed():
    num = e.get()
    e.delete(0, END)
    num = float(num)**3
    check_float(num)


def button_exponential():
    first_number = e.get()
    global f_num
    global math
    math = "expo"
    f_num = float(first_number)
    e.delete(0, END)


def button_eExpo():
    num = e.get()
    e.delete(0, END)
    num = exp(float(num))
    check_float(num)


def button_tenExpo():
    num = e.get()
    e.delete(0, END)
    num = pow(10, float(num))
    check_float(num)


def button_inverse():
    num = e.get()
    e.delete(0, END)
    num = 1/float(num)
    check_float(num)


def button_squareRoot():
    num = e.get()
    e.delete(0, END)
    num = sqrt(float(num))
    check_float(num)


def button_cubeRoot():
    num = e.get()
    e.delete(0, END)
    num = pow(float(num), 1/3)
    check_float(num)


def button_expoRoot():
    first_number = e.get()
    global f_num
    global math
    math = "root"
    f_num = float(first_number)
    e.delete(0, END)


def button_natLog():
    num = e.get()
    e.delete(0, END)
    num = log(float(num), exp(1))
    check_float(num)


def button_log():
    num = e.get()
    e.delete(0, END)
    num = log(float(num), 10)
    check_float(num)


def button_factorial():
    num = e.get()
    e.delete(0, END)
    num = factorial(float(num))
    check_float(num)


def button_sin():
    num = e.get()
    e.delete(0, END)
    num = sin(float(num))
    check_float(num)


def button_cos():
    num = e.get()
    e.delete(0, END)
    num = cos(float(num))
    check_float(num)


def button_tan():
    num = e.get()
    e.delete(0, END)
    num = tan(float(num))
    check_float(num)


def button_e():
    e.delete(0, END)
    e.insert(0, exp(1))


def button_EE():
    return


def button_Rad():
    return


def button_sinh():
    num = e.get()
    e.delete(0, END)
    num = sinh(float(num))
    check_float(num)


def button_cosh():
    num = e.get()
    e.delete(0, END)
    num = cosh(float(num))
    check_float(num)


def button_tanh():
    num = e.get()
    e.delete(0, END)
    num = tanh(float(num))
    check_float(num)


def button_pi():
    e.delete(0, END)
    e.insert(0, pi)


def button_Rand():
    e.delete(0, END)
    e.insert(0, random())


def city_name():
    name = city_entry.get()

    api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + name +
                               "&appid=9edec1cfeeedb9c0d42474a34ace0b48")
    api = json.loads(api_request.content)
    temperature = api["main"]["temp"]
    farenheit = ((temperature - 273.15)*(9/5)) + 32
    e.insert(0, "{:.2f}".format(farenheit))

    window.destroy()



def weather():
    e.delete(0, END)

    try:
        global window
        global city_entry

        window = Tk()
        window.title("Enter your city name")
        window.resizable(width=False, height=False)

        city_label = Label(window, text="Enter your city name:")
        city_entry = Entry(window)
        submit_button = Button(window, text="Submit", pady=10, command=city_name)

        city_label.grid(row=0, column=0)
        city_entry.grid(row=0, column=1)
        submit_button.grid(row=1, column=0, columnspan=2, sticky="ew")

    except:
        e.insert(0, "Error, check spelling")


def change_buttons():
    return


def button_2nd():
    global second

    if second == 0:
        second = 1

        button_weather = Button(root, text="Weather", pady=15, width=0, command=weather)
        button_weather.grid(row=5, column=4, columnspan=2, padx=(6, 0), sticky="ew")

    else:
        second = 0

        button_pi_second = Button(root, text="π", pady=15, command=button_pi)
        button_Rand_second = Button(root, text="Rand", pady=15, command=button_Rand)

        button_pi_second.grid(row=5, column=5, ipadx=20, sticky="ew")
        button_Rand_second.grid(row=5, column=4, ipadx=20, padx=(6, 0), sticky="ew")


# Create the frame for the Calculator GUI

root = Tk()
root.title("Christian Bloemhof's Calculator")
root.resizable(width=False, height=False)
root.geometry("243x330")

e = Entry(root)
e.grid(row=0, column=0, columnspan=4)


# Define Buttons ------------------------------------------------------------------------------------------------

# Number Buttons
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

# Basic Calculator Mathematics Features
button_adds    = Button(root, text="+",   pady=15, command=button_add)
button_subs    = Button(root, text="-",   pady=15, command=button_sub)
button_mults   = Button(root, text="x",   pady=15, command=button_mult)
button_divs    = Button(root, text="÷",   pady=15, command=button_div)
button_equals  = Button(root, text="=",   pady=15, command=button_equal)
button_clear   = Button(root, text="AC",  pady=15, command=button_clear)
button_sign    = Button(root, text="+/-", pady=15, command=button_sign)
button_percent = Button(root, text="%",   pady=15, command=button_percent)

# Buttons to adjust screen size
button_fullsize  = Button(root, text="Fullsize", pady=15, command=button_fullsize)
button_smallsize = Button(root, text="Smallsize", pady=15, command=button_smallsize)

# Row 1 Extra Buttons Creation
button_smile = Button(root, text=":)", pady=15, command=button_smile)
button_ms = Button(root, text="ms", pady=15, command=button_ms)
button_mc = Button(root, text="mc", pady=15, command=button_mc)
button_mPlus = Button(root, text="m+", pady=15, command=button_mPlus)
button_mMinus = Button(root, text="m-", pady=15, command=button_mMinus)
button_mr = Button(root, text="mr", pady=15, command=button_mr)

# Row 2 Extra Buttons Creation
button_2nd = Button(root, text="2nd", pady=15, command=button_2nd)
button_squared = Button(root, text="x^2", pady=15, command=button_squared)
button_cubed = Button(root, text="x^3", pady=15, command=button_cubed)
button_exponential = Button(root, text="x^y", pady=15, command=button_exponential)
button_eExpo = Button(root, text="e^x", pady=15, command=button_eExpo)
button_tenExpo = Button(root, text="10^x", pady=15, command=button_tenExpo)

# Row 3 Extra Buttons Creation
button_inverse = Button(root, text="1/x", pady=15, command=button_inverse)
button_squareRoot = Button(root, text="2√x", pady=15, command=button_squareRoot)
button_cubeRoot = Button(root, text="3√x", pady=15, command=button_cubeRoot)
button_expoRoot = Button(root, text="y√x", pady=15, command=button_expoRoot)
button_natLog = Button(root, text="ln", pady=15, command=button_natLog)
button_log = Button(root, text="log_10", pady=15, command=button_log)

# Row 4 Extra Buttons Creation
button_factorial = Button(root, text="x!", pady=15, command=button_factorial)
button_sin = Button(root, text="sin", pady=15, command=button_sin)
button_cos = Button(root, text="cos", pady=15, command=button_cos)
button_tan = Button(root, text="tan", pady=15, command=button_tan)
button_e = Button(root, text="e", pady=15, command=button_e)
button_EE = Button(root, text="EE", pady=15, command=button_EE)

# Row 5 Extra Buttons Creation
button_Rad = Button(root, text="Rad", pady=15, command=button_Rad)
button_sinh = Button(root, text="sinh", pady=15, command=button_sinh)
button_cosh = Button(root, text="cosh", pady=15, command=button_cosh)
button_tanh = Button(root, text="tanh", pady=15, command=button_tanh)
button_pi = Button(root, text="π", pady=15, command=button_pi)
button_Rand = Button(root, text="Rand", pady=15, command=button_Rand)

# Bind the buttons to the keys on the keyboard -------------------------------------------------------------

root.bind('<Key>', key_pressed)
root.bind('<Return>', button_equal)
root.bind('<+>', button_add)
root.bind('<minus>', button_sub)
root.bind('<*>', button_mult)
root.bind('</>', button_div)
root.bind('<%>', button_percent)

# Put the buttons on the screen in the correct order --------------------------------------------------------

button_fullsize.grid(row=6, column=0, columnspan=4, sticky="ew")
button_smallsize.grid(row=6, column=4, columnspan=6, padx=(6, 0), sticky="ew")

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
button_divs.grid(row=1, column=3, sticky="ew")

# Here's where the hidden buttons are inserted

# Row 1 Extra Buttons Placement

button_smile.grid(row=1, column=9, ipadx=20, sticky="ew")
button_ms.grid(row=1, column=8, ipadx=20, sticky="ew")
button_mc.grid(row=1, column=7, ipadx=20, sticky="ew")
button_mPlus.grid(row=1, column=6, ipadx=20, sticky="ew")
button_mMinus.grid(row=1, column=5, ipadx=20, sticky="ew")
button_mr.grid(row=1, column=4, ipadx=20, padx=(6, 0), sticky="ew")

# Row 2 Extra Buttons Placement

button_2nd.grid(row=2, column=9, ipadx=20, sticky="ew")
button_squared.grid(row=2, column=8, ipadx=20, sticky="ew")
button_cubed.grid(row=2, column=7, ipadx=20, sticky="ew")
button_exponential.grid(row=2, column=6, ipadx=20, sticky="ew")
button_eExpo.grid(row=2, column=5, ipadx=20, sticky="ew")
button_tenExpo.grid(row=2, column=4, ipadx=20, padx=(6, 0), sticky="ew")

# Row 3 Extra Buttons Placement

button_inverse.grid(row=3, column=9, ipadx=20, sticky="ew")
button_squareRoot.grid(row=3, column=8, ipadx=20, sticky="ew")
button_cubeRoot.grid(row=3, column=7, ipadx=20, sticky="ew")
button_expoRoot.grid(row=3, column=6, ipadx=20, sticky="ew")
button_natLog.grid(row=3, column=5, ipadx=20, sticky="ew")
button_log.grid(row=3, column=4, ipadx=15, padx=(6, 0), sticky="ew")

# Row 4 Extra Buttons Placement

button_factorial.grid(row=4, column=9, ipadx=20, sticky="ew")
button_sin.grid(row=4, column=8, ipadx=20, sticky="ew")
button_cos.grid(row=4, column=7, ipadx=20, sticky="ew")
button_tan.grid(row=4, column=6, ipadx=20, sticky="ew")
button_e.grid(row=4, column=5, ipadx=20, sticky="ew")
button_EE.grid(row=4, column=4, ipadx=20, padx=(6, 0), sticky="ew")

# Row 5 Extra Buttons Placement

button_Rad.grid(row=5, column=9, ipadx=20, sticky="ew")
button_sinh.grid(row=5, column=8, ipadx=20, sticky="ew")
button_cosh.grid(row=5, column=7, ipadx=20, sticky="ew")
button_tanh.grid(row=5, column=6, ipadx=20, sticky="ew")
button_pi.grid(row=5, column=5, ipadx=20, sticky="ew")
button_Rand.grid(row=5, column=4, ipadx=20, padx=(6, 0), sticky="ew")


root.mainloop()
