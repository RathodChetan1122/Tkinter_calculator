import tkinter as tk

# Function to evaluate expressions
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to add text to the entry field
def add_to_expression(value):
    entry.insert(tk.END, value)

# Function to clear the entry field
def clear_expression():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Colorful Calculator")

# Entry widget
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout with colors
buttons = [
    ("7", 1, 0, "#f0f8ff"), ("8", 1, 1, "#f0f8ff"), ("9", 1, 2, "#f0f8ff"), ("/", 1, 3, "#ffb6c1"),
    ("4", 2, 0, "#f0f8ff"), ("5", 2, 1, "#f0f8ff"), ("6", 2, 2, "#f0f8ff"), ("*", 2, 3, "#ffb6c1"),
    ("1", 3, 0, "#f0f8ff"), ("2", 3, 1, "#f0f8ff"), ("3", 3, 2, "#f0f8ff"), ("-", 3, 3, "#ffb6c1"),
    ("0", 4, 0, "#f0f8ff"), (".", 4, 1, "#f0f8ff"), ("+", 4, 2, "#ffb6c1"), ("=", 4, 3, "#90ee90"),
]

for (text, row, col, color) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, bg=color, fg="black", command=evaluate_expression)
    else:
        button = tk.Button(root, text=text, width=5, height=2, bg=color, fg="black", command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button with distinct color
clear_button = tk.Button(root, text="C", width=5, height=2, bg="#ffa07a", fg="black", command=clear_expression)
clear_button.grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)

root.mainloop()
