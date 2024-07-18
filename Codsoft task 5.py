



######## THIS IS A PROGRAM TO CREATE A CONTACT BOOK TO SAVE UPDATED AND DELETE CONTACTS ###########




import tkinter as tk
from tkinter import messagebox, simpledialog
import json

##### Initialize the contacts list #####
contacts = []

###### Load contacts from a file if it exists #####
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    pass

###### Function to save contacts to a file #####
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

###### Function to add a new contact #####
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

###### Function to view contacts in the listbox #####
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

###### Function to search contacts #####
def search_contact():
    query = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

###### Function to display contact details #####
def display_contact_details(event):
    selected_contact = listbox_contacts.curselection()
    if selected_contact:
        index = selected_contact[0]
        contact = contacts[index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact['name'])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact['phone'])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact['email'])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact['address'])

###### Function to update contact details #####
def update_contact():
    selected_contact = listbox_contacts.curselection()
    if selected_contact:
        index = selected_contact[0]
        contacts[index]['name'] = entry_name.get()
        contacts[index]['phone'] = entry_phone.get()
        contacts[index]['email'] = entry_email.get()
        contacts[index]['address'] = entry_address.get()
        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to update.")

###### Function to delete a contact #####
def delete_contact():
    selected_contact = listbox_contacts.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        save_contacts()
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

###### Function to clear entry fields #####
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

###### Create the main window #####
root = tk.Tk()
root.title("Contact Book")

###### Set a custom color scheme and font #####
root.configure(bg='#E6E6FA')
custom_font = ("Helvetica", 12)

###### Create and place the widgets #####
frame_inputs = tk.Frame(root, bg='#E6E6FA')
frame_inputs.pack(pady=10)

label_name = tk.Label(frame_inputs, text="Name:", font=custom_font, bg='#E6E6FA')
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_inputs, font=custom_font)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(frame_inputs, text="Phone:", font=custom_font, bg='#E6E6FA')
label_phone.grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_inputs, font=custom_font)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(frame_inputs, text="Email:", font=custom_font, bg='#E6E6FA')
label_email.grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_inputs, font=custom_font)
entry_email.grid(row=2, column=1, padx=5, pady=5)

label_address = tk.Label(frame_inputs, text="Address:", font=custom_font, bg='#E6E6FA')
label_address.grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(frame_inputs, font=custom_font)
entry_address.grid(row=3, column=1, padx=5, pady=5)

frame_buttons = tk.Frame(root, bg='#E6E6FA')
frame_buttons.pack(pady=10)

button_add = tk.Button(frame_buttons, text="Add Contact", font=custom_font, command=add_contact)
button_add.grid(row=0, column=0, padx=5, pady=5)

button_update = tk.Button(frame_buttons, text="Update Contact", font=custom_font, command=update_contact)
button_update.grid(row=0, column=1, padx=5, pady=5)

button_delete = tk.Button(frame_buttons, text="Delete Contact", font=custom_font, command=delete_contact)
button_delete.grid(row=0, column=2, padx=5, pady=5)

frame_search = tk.Frame(root, bg='#E6E6FA')
frame_search.pack(pady=10)

label_search = tk.Label(frame_search, text="Search:", font=custom_font, bg='#E6E6FA')
label_search.grid(row=0, column=0, padx=5, pady=5)
entry_search = tk.Entry(frame_search, font=custom_font)
entry_search.grid(row=0, column=1, padx=5, pady=5)
button_search = tk.Button(frame_search, text="Search", font=custom_font, command=search_contact)
button_search.grid(row=0, column=2, padx=5, pady=5)

frame_listbox = tk.Frame(root, bg='#E6E6FA')
frame_listbox.pack(pady=10)

listbox_contacts = tk.Listbox(frame_listbox, font=custom_font, width=50, height=10)
listbox_contacts.pack(side=tk.LEFT, padx=5, pady=5)
listbox_contacts.bind("<<ListboxSelect>>", display_contact_details)

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_contacts.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_contacts.yview)

update_contact_list()

###### Run the main loop #####
root.mainloop()
