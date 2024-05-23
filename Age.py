import tkinter as tk
from tkinter import messagebox

def process_id():
    x = entry.get()
    if len(x) < 7 or not x.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid ID number.")
        return

    y = x[0:4]
    z = x[4:7]
    q = int(z)

    gender = "Female" if q > 500 else "Male"
    if q > 500:
        q -= 500

    k = "Your Birthday Is On"

    if q <= 0 or q > 366:
        messagebox.showerror("Input Error", "Invalid day of year in ID number.")
        return

    if q <= 31:
        month = "January"
        day = q
    elif q <= 60:
        month = "February"
        day = q - 31
    elif q <= 91:
        month = "March"
        day = q - 60
    elif q <= 121:
        month = "April"
        day = q - 91
    elif q <= 152:
        month = "May"
        day = q - 121
    elif q <= 182:
        month = "June"
        day = q - 152
    elif q <= 213:
        month = "July"
        day = q - 182
    elif q <= 244:
        month = "August"
        day = q - 213
    elif q <= 274:
        month = "September"
        day = q - 244
    elif q <= 305:
        month = "October"
        day = q - 274
    elif q <= 335:
        month = "November"
        day = q - 305
    else:
        month = "December"
        day = q - 335

    result = f"{k} {y}, {month} {day}\nGender: {gender}"
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("ID Number Processor")

# Set the font size
font = ("Helvetica", 16)

# Create and place the widgets
tk.Label(root, text="Enter Your ID Number:", font=font).pack(pady=10)
entry = tk.Entry(root, font=font)
entry.pack(pady=5)

process_button = tk.Button(root, text="Process", command=process_id, font=font)
process_button.pack(pady=10)

result_label = tk.Label(root, text="", font=font)
result_label.pack(pady=20)

# Run the main loop
root.mainloop()
