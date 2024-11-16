import tkinter as tk
from tkinter import messagebox

def perform_operation(operation):
    """Perform the selected arithmetic operation."""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation!")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

def clear_inputs():
    """Clear the input fields and result label."""
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main application window
app = tk.Tk()
app.title("Calculator")
app.geometry("300x400")

# Widgets for input
tk.Label(app, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(app, width=20)
entry1.pack(pady=5)

tk.Label(app, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(app, width=20)
entry2.pack(pady=5)

# Label to display the result
result_label = tk.Label(app, text="Result: ", font=("Arial", 12))
result_label.pack(pady=20)

# Operation buttons
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

tk.Button(button_frame, text="+", width=5, command=lambda: perform_operation("+")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="-", width=5, command=lambda: perform_operation("-")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="*", width=5, command=lambda: perform_operation("*")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="/", width=5, command=lambda: perform_operation("/")).grid(row=1, column=1, padx=5, pady=5)

# Clear button
clear_button = tk.Button(app, text="Clear", command=clear_inputs, width=10, bg="red", fg="white")
clear_button.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
