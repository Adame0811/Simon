import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("A Little Question for You")
root.geometry("500x300")

question = tk.Label(root, text="Lita's tapos libre nak niya bay?", font=("Arial", 18))
question.pack(pady=40)

# Function to show response to "Yes"
def yes_clicked():
    response = tk.Label(root, text="Thanks Bay", font=("Arial", 16), fg="green")
    response.pack()

# Function to move "No" button randomly
def no_hover(event):
    no_button.place(x=random.randint(50, 400), y=random.randint(150, 250))

# Yes Button
yes_button = tk.Button(root, text="Yes", font=("Arial", 14), bg="lightgreen", command=yes_clicked)
yes_button.place(x=150, y=200)

# No Button
no_button = tk.Button(root, text="No", font=("Arial", 14), bg="lightcoral")
no_button.place(x=250, y=200)
no_button.bind("<Enter>", no_hover)  # When mouse hovers, button moves

root.mainloop()
