import tkinter as tk
from tkinter import messagebox

# calculation Function
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

# Create the main window
root = tk.Tk()
root.title("Njongo's Calculator")

# Create and place widgets
tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

tk.Label(root, text="Operation:").grid(row=2, column=0)
combo_operation = tk.StringVar()
combo_operation.set("Addition")  # default value
operation_menu = tk.OptionMenu(root, combo_operation, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.grid(row=2, column=1)

btn_calculate = tk.Button(root, text="Calculate", command=calculate)
btn_calculate.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, columnspan=2)

# Run the application
root.mainloop()
