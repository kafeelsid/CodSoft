import tkinter as tk


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")


# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0)

operation_var = tk.StringVar(root)
operation_var.set('+')  # Default operation is addition
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=0, column=1)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=2)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1)

# Create result label
result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0, columnspan=3)

# Run the main event loop
root.mainloop()
