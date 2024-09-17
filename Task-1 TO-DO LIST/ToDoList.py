# CODSOFT/Python programming internship/Task 1/TO-DO LIST

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

# Function to add a new task
def add_task():
    task_name = task_entry.get()
    due_date = due_date_entry.get()
    if task_name and due_date:
        try:
            # Change date format to DD-MM-YYYY
            datetime.strptime(due_date, "%d-%m-%Y")
            tasks_listbox.insert(tk.END, f"{task_name} | {due_date} | Pending")
            task_entry.delete(0, tk.END)
            due_date_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in DD-MM-YYYY format.")
    else:
        messagebox.showwarning("Input Error", "Please enter a task and due date.")

# Function to update a selected task
def update_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        updated_task_name = simpledialog.askstring("Update Task", "Enter new task name:")
        updated_due_date = simpledialog.askstring("Update Due Date", "Enter new due date (DD-MM-YYYY):")
        if updated_task_name and updated_due_date:
            datetime.strptime(updated_due_date, "%d-%m-%Y")
            task_status = tasks_listbox.get(selected_task_index).split("|")[2].strip()  # Preserve the status
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, f"{updated_task_name} | {updated_due_date} | {task_status}")
        else:
            messagebox.showwarning("Input Error", "Both task name and due date are required.")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in DD-MM-YYYY format.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task_info = tasks_listbox.get(selected_task_index)
        if "Pending" in task_info:
            task_info = task_info.replace("Pending", "Completed")
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, task_info)
        else:
            messagebox.showinfo("Task Status", "Task is already completed.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to clear all tasks
def clear_all_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        tasks_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Main background color
bg_color = "#FFFFFF"

root.config(bg=bg_color)

# Set window size to 500x500
root.geometry("500x600")

# Header Frame
header_frame = tk.Frame(root, bg=bg_color, pady=15)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="To-Do List", font=("Times New Roman", 20, "bold"), fg="black", bg=bg_color)
header_label.pack()

# Input Frame for Task and Due Date
input_frame = tk.Frame(root, bg=bg_color, pady=10)
input_frame.pack(pady=10)

task_label = tk.Label(input_frame, text="Task :", font=("Helvetica", 12), bg=bg_color, fg="black")
task_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

task_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 12), relief="solid", highlightthickness=1, highlightbackground="#dcdcdc")
task_entry.grid(row=0, column=1, padx=10, pady=5)

due_date_label = tk.Label(input_frame, text="Due Date (DD-MM-YYYY) :", font=("Helvetica", 12), bg=bg_color, fg="black")
due_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

due_date_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 12), relief="solid", highlightthickness=1, highlightbackground="#dcdcdc")
due_date_entry.grid(row=1, column=1, padx=10, pady=5)

# Listbox to display tasks with columns
tasks_listbox_frame = tk.Frame(root, bg=bg_color, padx=10, pady=10)
tasks_listbox_frame.pack()

# Listbox to show tasks
tasks_listbox = tk.Listbox(tasks_listbox_frame, width=45, height=10, font=("Helvetica", 12), relief="solid", bg="white", fg="black", 
                           selectbackground="#4CAF50", selectforeground="white")
tasks_listbox.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg=bg_color, pady=10)
button_frame.pack()

def create_button(text, command, color):
    return tk.Button(button_frame, text=text, command=command, font=("Helvetica", 10, "bold"), bg=color, fg="white", relief="flat", width=15, height=2)

add_button = create_button("Add Task", add_task, "#4CAF50")
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = create_button("Update Task", update_task, "#FF9800")
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = create_button("Delete Task", delete_task, "#F44336")
delete_button.grid(row=1, column=0, padx=5, pady=5)

complete_button = create_button("Mark as Completed", mark_completed, "#2196F3")
complete_button.grid(row=1, column=1, padx=5, pady=5)

clear_button = create_button("Clear All Tasks", clear_all_tasks, "#6c757d")
clear_button.grid(row=2, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
