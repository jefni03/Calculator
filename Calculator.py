import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Calculator")
root.geometry("570x600")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""
previous_equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation, previous_equation
    result = ""

    if equation != "":
        try:
            equation = equation.replace('÷', '/')
            equation = equation.replace('x', '*')

            result = eval(equation)

            if result.is_integer():
                result = int(result)
            else:
                result = round(result, 10)
                result = '{:.10f}'.format(result).rstrip('0')

            previous_equation = equation
            equation = str(result)
        except ZeroDivisionError:
            result = "Error: Division by zero"
            equation = ""
        except Exception as e:
            result = "Error"
            equation = ""

    label_result.config(text=result)

    label_previous.config(text=previous_equation + " =")
    label_previous.place(x=root.winfo_reqwidth() - label_previous.winfo_reqwidth() - 10, y=0)

def toggle_sign():
    global equation
    if equation and equation[0] == '-':
        equation = equation[1:]
    else:
        equation = '-' + equation
    label_result.config(text=equation)

def percent():
    global equation
    equation = str(eval(equation) / 100)
    label_result.config(text=equation)

label_result = tk.Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

label_previous = tk.Label(root, text="", font=("Helvetica", 16, "bold"), fg="darkgrey")
label_previous.place(x=490, y=10)


Button(root, text="C", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="darkgrey", command=lambda: clear()).place(x=10, y=100)
Button(root, text="+/-", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="darkgrey", command=lambda: toggle_sign()).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="darkgrey", command=lambda: percent()).place(x=290, y=100)
Button(root, text="÷", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="orange", command=lambda: show("÷")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="x", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="orange", command=lambda: show("x")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="-", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="orange", command=lambda: show("-")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="+", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="orange", command=lambda: show("+")).place(x=430, y=400)

Button(root, text="0", width=11, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show("0")).place(x=10, y=500)
Button(root, text=".", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: show(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="white", bg="grey", command=lambda: calculate()).place(x=430, y=500)




root.mainloop()