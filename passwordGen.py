import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        # Define the characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generating a random passwod
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Displaying the password 
        label_result.config(text=f"Generated Password: {password}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Creating the main window here Tkinter
root = tk.Tk()
root.title("Njongo's Password Generator")


tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Generated Password:")
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
