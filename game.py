import tkinter as tk
from tkinter import messagebox
import random

def play(choice):
    # List of choices
    choices = ['rock', 'paper', 'scissors']
    
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Determine the result
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == 'rock' and computer_choice == 'scissors') or \
         (choice == 'scissors' and computer_choice == 'paper') or \
         (choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        global user_score
        user_score += 1
    else:
        result = "You lose!"
        global computer_score
        computer_score += 1

    # Update the results
    label_user_choice.config(text=f"Your Choice: {choice.capitalize()}")
    label_computer_choice.config(text=f"Computer's Choice: {computer_choice.capitalize()}")
    label_result.config(text=result)
    label_user_score.config(text=f"Your Score: {user_score}")
    label_computer_score.config(text=f"Computer's Score: {computer_score}")
    
    # Ask to play again
    if messagebox.askyesno("Play Again", "Do you want to play another round?"):
        reset_game()
    else:
        root.quit()

def reset_game():
    # Reset the game for a new round
    label_user_choice.config(text="Your Choice: ")
    label_computer_choice.config(text="Computer's Choice: ")
    label_result.config(text="")
    
def create_choice_buttons():
    # Create buttons for rock, paper, and scissors
    tk.Button(root, text="Rock", command=lambda: play('rock')).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(root, text="Paper", command=lambda: play('paper')).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="Scissors", command=lambda: play('scissors')).grid(row=1, column=2, padx=10, pady=10)

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Njongo's Rock, Paper, Scissors")

# Create and place widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors:").grid(row=0, column=0, columnspan=3, padx=10, pady=10)

create_choice_buttons()

label_user_choice = tk.Label(root, text="Your Choice: ")
label_user_choice.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

label_computer_choice = tk.Label(root, text="Computer's Choice: ")
label_computer_choice.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

label_user_score = tk.Label(root, text="Your Score: 0")
label_user_score.grid(row=5, column=0, padx=10, pady=5)

label_computer_score = tk.Label(root, text="Computer's Score: 0")
label_computer_score.grid(row=5, column=2, padx=10, pady=5)

# Run the application
root.mainloop()
