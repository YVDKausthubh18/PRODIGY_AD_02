import tkinter as tk
from tkinter import messagebox
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")      
        edit_entry = tk.Entry(edit_window, width=30)
        edit_entry.insert(0, selected_task)
        edit_entry.pack(pady=10)
        def update_task():
            new_task = edit_entry.get()
            if new_task:
                listbox.delete(selected_task_index)
                listbox.insert(selected_task_index, new_task)
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        update_button = tk.Button(edit_window, text="Update Task", command=update_task, bg="lightblue")
        update_button.pack(pady=5)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
root = tk.Tk()
root.title("To-Do List")
root.configure(bg="white")
entry = tk.Entry(root, width=130)
entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task, bg="lightgreen")
add_button.pack(pady=10)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=130, height=10, bg="lightyellow")
listbox.pack(pady=10)
edit_button = tk.Button(root, text="Edit Task", command=edit_task, bg="lightblue", fg="white")
edit_button.pack(pady=15)
delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="salmon", fg="white")
delete_button.pack(pady=15)
root.mainloop()
