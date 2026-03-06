import tkinter as tk

# Create window
window = tk.Tk()
window.title("My First Frontend App")
window.geometry("40x20")

# Function
def show_message():
    label.config(text="Hello Siddarth! Welcome to Python Frontend")

# Label
label = tk.Label(window, text="Click the button", font=("Arial", 14))
label.pack(pady=20)

# Button
button = tk.Button(window, text="Click Me", command=show_message)
button.pack()

# Run application
window.mainloop()
