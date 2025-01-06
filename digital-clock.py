# installing required packages
# pip install tk

# importing required packages
import tkinter as tk
from time import strftime
from datetime import datetime

root = tk.Tk()
root.title("Python Digital Clock")

# define the clock label
clock_label = tk.Label(root,
                       font=("Helvetica", 54),
                       bg="black", fg="cyan")
clock_label.pack(anchor="center", fill="both", expand=True)

# # function to update the clock - for HH:MM:SS format
# def updateClock():
#     current_time = strftime("%H:%M:%S:%S")
#     clock_label.config(text=current_time)
#     clock_label.after(1000, updateClock)

# function to update the clock - for HH:MM:SS:MS format
def updateClock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") + f":{now.microsecond // 1000:03d}"  # Add milliseconds
    clock_label.config(text=current_time)
    clock_label.after(100, updateClock)  # Update every 100 ms for smooth display

# starting the clock
updateClock()
root.mainloop()