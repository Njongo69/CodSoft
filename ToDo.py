import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Njongo's To-Do List")

        self.tasks = []

        #UI components
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        
        self.add_button =tk.Button(self.frame, text="Add A Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.tasks_listbox = tk.Listbox(self.root, width=70, height=15)
        self.tasks_listbox.pack(pady=10)

        self.update_button = tk.Button(self.root, text="Mark Task As Done",command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task",command=self.delete_task)
        self.update_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'title': task, 'completed': False})
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You Are Required To Enter A Task!")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "Done ✔" if task['completed'] else "Not Done ❌"
            self.tasks_listbox.insert(tk.END, f"{i + 1}. {task['title']} - {status}")

    def update_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("warning", "Select A Taks To Update!")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "Select A Task To Delete!")

        
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()



