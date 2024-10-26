import tkinter as tk

def click_button(item):
    current_text = input_text.get()
    input_text.set(current_text + str(item))

def clear():
    input_text.set("")

def calculate():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except:
        input_text.set("Erro")

root = tk.Tk()
root.title("Calculadora")

input_text = tk.StringVar()

input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 18), bd=10, insertwidth=4, width=14, borderwidth=4)
input_field.grid(row=0, column=0)
input_field.pack()

buttons_frame = tk.Frame(root)
buttons_frame.pack()

button1 = tk.Button(buttons_frame, text="1", width=10, height=3, command=lambda: click_button(1))
button1.grid(row=1, column=0)

button2 = tk.Button(buttons_frame, text="2", width=10, height=3, command=lambda: click_button(2))
button2.grid(row=1, column=1)

button3 = tk.Button(buttons_frame, text="3", width=10, height=3, command=lambda: click_button(3))
button3.grid(row=1, column=2)

button4 = tk.Button(buttons_frame, text="4", width=10, height=3, command=lambda: click_button(4))
button4.grid(row=2, column=0)

button5 = tk.Button(buttons_frame, text="5", width=10, height=3, command=lambda: click_button(5))
button5.grid(row=2, column=1)

button6 = tk.Button(buttons_frame, text="6", width=10, height=3, command=lambda: click_button(6))
button6.grid(row=2, column=2)

button7 = tk.Button(buttons_frame, text="7", width=10, height=3, command=lambda: click_button(7))
button7.grid(row=3, column=0)

button8 = tk.Button(buttons_frame, text="8", width=10, height=3, command=lambda: click_button(8))
button8.grid(row=3, column=1)

button9 = tk.Button(buttons_frame, text="9", width=10, height=3, command=lambda: click_button(9))
button9.grid(row=3, column=2)

button0 = tk.Button(buttons_frame, text="0", width=10, height=3, command=lambda: click_button(0))
button0.grid(row=4, column=1)

plus_button = tk.Button(buttons_frame, text="+", width=10, height=3, command=lambda: click_button("+"))
plus_button.grid(row=1, column=3)

minus_button = tk.Button(buttons_frame, text="-", width=10, height=3, command=lambda: click_button("-"))
minus_button.grid(row=2, column=3)

multiply_button = tk.Button(buttons_frame, text="*", width=10, height=3, command=lambda: click_button("*"))
multiply_button.grid(row=3, column=3)

divide_button = tk.Button(buttons_frame, text="/", width=10, height=3, command=lambda: click_button("/"))
divide_button.grid(row=4, column=3)

equal_button = tk.Button(buttons_frame, text="=", width=10, height=3, command=calculate)
equal_button.grid(row=4, column=2)

clear_button = tk.Button(buttons_frame, text="C", width=10, height=3, command=clear)
clear_button.grid(row=4, column=0)

root.mainloop()

