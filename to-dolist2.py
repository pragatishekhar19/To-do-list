import tkinter as tk
from tkinter import ttk, messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Configure style
style = ttk.Style()
style.configure('TButton', font=('Comic Sans MS', 12), padding=5, background='#4CAF50', foreground='red')
style.configure('TEntry', font=('Comic Sans MS', 12), padding=5, background='#FFD700')
style.configure('TListbox', font=('Comic Sans MS', 12), padding=5, background='#E0E0E0', selectbackground='#4CAF50', selectforeground='red')

# Create and pack the listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE, bd=0, activestyle="none")
listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Create and pack the entry widget
entry = ttk.Entry(root, style='TEntry')
entry.pack(pady=5, padx=20, fill=tk.X)

# Create and pack the add and delete buttons
add_button = ttk.Button(root, text="Add Task", command=add_task, style='TButton', cursor='hand2')
add_button.pack(side=tk.LEFT, padx=5)
delete_button = ttk.Button(root, text="Delete Task", command=delete_task, style='TButton', cursor='hand2')
delete_button.pack(side=tk.RIGHT, padx=5)

# Start the main loop
root.mainloop()
