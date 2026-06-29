from tkinter import *

# Window
root = Tk()
root.title("Calculator")
root.geometry("320x450")

# Display
entry = Entry(root, width=16, font=("Arial", 24), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Function to add numbers/operators
def click(value):
    entry.insert(END, value)

# Clear screen
def clear():
    entry.delete(0, END)

# Calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons
for (text, row, col) in buttons:
    
    if text == "C":
        btn = Button(root, text=text, padx=20, pady=20,
                     font=("Arial", 14), command=clear)

    elif text == "=":
        btn = Button(root, text=text, padx=20, pady=20,
                     font=("Arial", 14), command=equal)

    else:
        btn = Button(root, text=text, padx=20, pady=20,
                     font=("Arial", 14),
                     command=lambda t=text: click(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

# Run app
root.mainloop()
