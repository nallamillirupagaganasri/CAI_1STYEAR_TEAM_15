# Simple Tkinter Quiz App
# Question: In which year Python was introduc

from tkinter import *
from tkinter import messagebox   # for showing pop-up messages

# Step 1: Create the main window
root = Tk()
root.title("Python Quiz App")        # window title
root.geometry("400x300")             # window size (Width x Height)
root.config(bg="lightblue")          # background color

# Step 2: Add the question label
question = Label(
    root,
    text="In which year was Python introduced?",
    font=("Arial", 14),
    bg="lightblue",
    fg="darkblue",
    wraplength=350,                  # makes text fit nicely
    justify="center"
)
question.pack(pady=20)

# Step 3: Store correct answer
correct_answer = "B"

# Step 4: Function to check user's answer
def check_answer(selected_option):
    if selected_option == correct_answer:
        messagebox.showinfo("Result", " Correct! Python was introduced in 1991.")
    else:
        messagebox.showerror("Result", " Wrong! The correct answer is 1991.")

# Step 5: Create multiple-choice buttons
button_a = Button(root, text="A. 1989", width=20, command=lambda: check_answer("A"))
button_a.pack(pady=5)

button_b = Button(root, text="B. 1991", width=20, command=lambda: check_answer("B"))
button_b.pack(pady=5)

button_c = Button(root, text="C. 1995", width=20, command=lambda: check_answer("C"))
button_c.pack(pady=5)

button_d = Button(root, text="D. 2000", width=20, command=lambda: check_answer("D"))
button_d.pack(pady=5)

# Step 6: Run the main event loop (shows the window)
root.mainloop()