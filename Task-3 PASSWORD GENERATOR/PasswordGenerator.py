# CODSOFT/Python programming internship/Task 3/PASSWORD GENERATOR

import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    char_sets = {
        'low': string.ascii_lowercase,
        'medium': string.ascii_letters,
        'high': string.ascii_letters + string.digits,
        'very_high': string.ascii_letters + string.digits + string.punctuation
    }
    
    # Choose the character set based on the specified complexity
    chars = char_sets.get(complexity, string.ascii_letters)
    
    # Generate a random password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def on_generate_click():
    try:
        length = int(length_entry.get())
        complexity = complexity_combobox.get().lower()
        
        if length <= 0:
            result_label.config(text="Length must be a positive integer.")
            return
        
        if not complexity:
            result_label.config(text="Please select a complexity level.")
            return
        
        password = generate_password(length, complexity)
        result_label.config(text=f"Generated Password :\n{password}")
    except ValueError:
        result_label.config(text="Please enter a valid number for length.")

def on_clear_click():
    length_entry.delete(0, tk.END)
    complexity_combobox.set("")
    result_label.config(text="Generated Password will appear here.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Create and place widgets with improved layout
tk.Label(root, text="Password Generator", font=("Times New Roman", 18, "bold"), bg="#f0f0f0").pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Enter Length :", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky='e')
length_entry = tk.Entry(frame, width=20)
length_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Complexity Level :", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky='e')
complexity_combobox = ttk.Combobox(frame, values=["low", "medium", "high", "very_high"], width=17)
complexity_combobox.grid(row=1, column=1, padx=10, pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Password", command=on_generate_click, width=20)
generate_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=on_clear_click, width=20)
clear_button.grid(row=0, column=1, padx=5)

result_label = tk.Label(root, text="Generated Password will appear here.", font=("Helvetica", 12), bg="#f0f0f0", wraplength=350, justify='center')
result_label.pack(pady=10)

# Run the application
root.mainloop()

