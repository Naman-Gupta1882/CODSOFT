

#####  THIS IS A PROGRAM FOR A SIMPLE CALCULATOR  ####### 





import tkinter as tk
from tkinter import messagebox
from math import sqrt

######### Function to perform the calculation ########
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        elif operation == '√':
            result = sqrt(num1)
        elif operation == '^':
            result = num1 ** num2

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

######### Create the main window ########
root = tk.Tk()
root.title("Personalized Calculator")

######## Set a custom color scheme ########
root.configure(bg='#F0F8FF')
custom_font = ("Helvetica", 12)

###### Create and place the widgets #######
label_welcome = tk.Label(root, text="Welcome to Naman's Calculator!", font=("Helvetica", 16, "bold"), bg='#F0F8FF')
label_welcome.grid(row=0, column=0, columnspan=4, pady=10)

label_num1 = tk.Label(root, text="Enter first number:", font=custom_font, bg='#F0F8FF')
label_num1.grid(row=1, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root, font=custom_font)
entry_num1.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

label_num2 = tk.Label(root, text="Enter second number:", font=custom_font, bg='#F0F8FF')
label_num2.grid(row=2, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, font=custom_font)
entry_num2.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

button_add = tk.Button(root, text="+", width=5, font=custom_font, command=lambda: calculate('+'))
button_add.grid(row=3, column=0, padx=5, pady=10)

button_subtract = tk.Button(root, text="-", width=5, font=custom_font, command=lambda: calculate('-'))
button_subtract.grid(row=3, column=1, padx=5, pady=10)

button_multiply = tk.Button(root, text="*", width=5, font=custom_font, command=lambda: calculate('*'))
button_multiply.grid(row=3, column=2, padx=5, pady=10)

button_divide = tk.Button(root, text="/", width=5, font=custom_font, command=lambda: calculate('/'))
button_divide.grid(row=3, column=3, padx=5, pady=10)

button_sqrt = tk.Button(root, text="√", width=5, font=custom_font, command=lambda: calculate('√'))
button_sqrt.grid(row=4, column=0, padx=5, pady=10)

button_power = tk.Button(root, text="^", width=5, font=custom_font, command=lambda: calculate('^'))
button_power.grid(row=4, column=1, padx=5, pady=10)

label_result = tk.Label(root, text="Result: ", font=("Helvetica", 14), bg='#F0F8FF')
label_result.grid(row=5, column=0, columnspan=4, pady=10)

######### Run the main loop ########
root.mainloop()
