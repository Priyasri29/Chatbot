import tkinter as tk

# Function to perform basic math operations
def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, f"\nYou: {expression}")
        chat.insert(tk.END, f"\nBot: {result}")
        chat.config(state=tk.DISABLED)
    except:
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, f"\nYou: {expression}")
        chat.insert(tk.END, f"\nBot: Error! Please check your input.")
        chat.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Create a new window
root = tk.Tk()
root.title("Math Chatbot")

# Create a chat window
chat = tk.Text(root, state=tk.DISABLED, height=20, width=50)
chat.pack()

# Create a label and entry for user input
input_label = tk.Label(root, text="Enter an expression:")
input_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to perform the calculation
button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

root.mainloop()