



######## THIS IS A PROGRAM FOR A PASSWORD GENRATOR #####




import random
import string
import tkinter as tk
from tkinter import messagebox

#########  Function to generate the password ######## 
def generate_password():
    try:
        length = int(entry_length.get())
        num_passwords = int(entry_num_passwords.get())
        if length <= 0 or num_passwords <= 0:
            raise ValueError("Length and number of passwords must be positive")

        include_uppercase = var_uppercase.get()
        include_lowercase = var_lowercase.get()
        include_digits = var_digits.get()
        include_special = var_special.get()

        if not (include_uppercase or include_lowercase or include_digits or include_special):
            raise ValueError("At least one character type must be selected")

        characters = ""
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        passwords = []
        for _ in range(num_passwords):
            password = ''.join(random.choice(characters) for _ in range(length))
            passwords.append(password)

        label_result.config(text=f"Generated Passwords:\n" + "\n".join(passwords))
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

#########  Create the main window  ######## 
root = tk.Tk()
root.title("Advanced Password Generator")

#########  Set a custom color scheme and font ######## 
root.configure(bg='#E6E6FA')
custom_font = ("Helvetica", 12)

#########  Create and place the widgets ######## 
label_intro = tk.Label(root, text="Welcome to the Advanced Password Generator!", font=("Helvetica", 16, "bold"), bg='#E6E6FA')
label_intro.grid(row=0, column=0, columnspan=2, pady=10)

label_length = tk.Label(root, text="Enter the desired length of the password:", font=custom_font, bg='#E6E6FA')
label_length.grid(row=1, column=0, padx=10, pady=10)

entry_length = tk.Entry(root, font=custom_font)
entry_length.grid(row=1, column=1, padx=10, pady=10)

label_num_passwords = tk.Label(root, text="Enter the number of passwords to generate:", font=custom_font, bg='#E6E6FA')
label_num_passwords.grid(row=2, column=0, padx=10, pady=10)

entry_num_passwords = tk.Entry(root, font=custom_font)
entry_num_passwords.grid(row=2, column=1, padx=10, pady=10)

var_uppercase = tk.BooleanVar()
check_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, font=custom_font, bg='#E6E6FA')
check_uppercase.grid(row=3, column=0, columnspan=2, pady=5)

var_lowercase = tk.BooleanVar()
check_lowercase = tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase, font=custom_font, bg='#E6E6FA')
check_lowercase.grid(row=4, column=0, columnspan=2, pady=5)

var_digits = tk.BooleanVar()
check_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits, font=custom_font, bg='#E6E6FA')
check_digits.grid(row=5, column=0, columnspan=2, pady=5)

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, font=custom_font, bg='#E6E6FA')
check_special.grid(row=6, column=0, columnspan=2, pady=5)

button_generate = tk.Button(root, text="Generate Passwords", font=custom_font, command=generate_password)
button_generate.grid(row=7, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Generated Passwords: ", font=("Helvetica", 14), bg='#E6E6FA')
label_result.grid(row=8, column=0, columnspan=2, pady=10)

#########  Run the main loop ######## 
root.mainloop()
