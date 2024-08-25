import tkinter as tk
from tkinter import messagebox

#  I create contacts list here
contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showerror("Error", "Name and phone number are required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    update_contact_list()
    clear_entries()

def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def view_contact_details(event):
    try:
        selected_index = listbox_contacts.curselection()[0]
        contact = contacts[selected_index]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact['name'])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact['phone'])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact['email'])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact['address'])
    except IndexError:
        pass

def update_contact():
    try:
        selected_index = listbox_contacts.curselection()[0]
        contacts[selected_index] = {
            "name": entry_name.get(),
            "phone": entry_phone.get(),
            "email": entry_email.get(),
            "address": entry_address.get()
        }
        update_contact_list()
        clear_entries()
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def delete_contact():
    try:
        selected_index = listbox_contacts.curselection()[0]
        contacts.pop(selected_index)
        update_contact_list()
        clear_entries()
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# my main window using tkinter obviously
root = tk.Tk()
root.title("Njongo's Contact Management")

# widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=2, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=3, padx=10, pady=10)

tk.Label(root, text="Search:").grid(row=5, column=0, padx=10, pady=5)
entry_search = tk.Entry(root)
entry_search.grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Search", command=search_contact).grid(row=5, column=2, padx=10, pady=5)

listbox_contacts = tk.Listbox(root, width=50, height=10)
listbox_contacts.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
listbox_contacts.bind('<<ListboxSelect>>', view_contact_details)

# lastly I then run the application
root.mainloop()
