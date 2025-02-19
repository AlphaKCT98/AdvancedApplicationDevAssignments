# Program Name: Assignment3.py
# Course: IT3883/Section W02
# Student Name: Keyvon Thompson
# Assignment Number: Lab3
# Due Date: 02/19/2025
# Purpose: This program converts miles per gallon (mpg) to kilometers
#          per liter (km/l) via a console-based interface.

import tkinter as tk

# Conversion factor (1 mpg = 0.425143707 km/l)
MPG_TO_KM_PER_L = 0.425143707

def convert_mpg_to_kml(*args):
    """
    Reads the mpg value from the input field. If it's valid, converts
    to km/l and displays the result. If invalid or empty, clears the output.
    """
    try:
        mpg_value = float(mpg_entry_var.get())
        km_per_l_value = mpg_value * MPG_TO_KM_PER_L
        result_label_var.set(f"{km_per_l_value:.4f} km/l")
    except ValueError:
        # Invalid or blank input; clear the result
        result_label_var.set("")

# Create the main window
root = tk.Tk()
root.title("MPG to km/l Converter")

# Variables that hold the user input and the result text
mpg_entry_var = tk.StringVar()
result_label_var = tk.StringVar()

# Whenever the user modifies the input string, call convert_mpg_to_kml
mpg_entry_var.trace_add("write", convert_mpg_to_kml)

# Create and place labels and entry fields
tk.Label(root, text="Enter mpg:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
mpg_entry = tk.Entry(root, textvariable=mpg_entry_var)
mpg_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Result in km/l:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
result_label = tk.Label(root, textvariable=result_label_var, fg="blue")
result_label.grid(row=1, column=1, padx=5, pady=5)

# Give focus to the input field
mpg_entry.focus()

# Run the application
root.mainloop()
