import tkinter as tk
from tkinter import messagebox
import random

class NoguessGame:
    def __init__(self, master):  
        self.master = master
        self.master.title("No. Guessing Game")
        self.hid_number = random.randint(1, 20)
        self.trial = 0

        # Label
        self.label = tk.Label(master, text="Guess a number between 1 and 20:")
        self.label.pack()

        # Input box
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Buttons
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game)
        self.new_game_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.master.quit)
        self.exit_button.pack()

    def check_guess(self):
        guess = self.entry.get().strip()  

        # special commands
        if guess.lower() == 'x':  # Exit 
            self.master.quit()
            return
        elif guess.lower() == 's':  # Show the hidden number
            messagebox.showinfo("Hint", f"The hidden number is: {self.hid_number}")
            return
        elif guess.lower() == 'n':  # new game
            self.new_game()
            return

        # Validate input 
        if not guess.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")
            return

        guess = int(guess)  # Convert to an integer
        self.trial += 1

        # Compare the guess with the hidden number
        if guess < self.hid_number:
            messagebox.showinfo("Result", "Too small!")
        elif guess > self.hid_number:
            messagebox.showinfo("Result", "Too big!")
        else:
            messagebox.showinfo(
                "Congratulations",
                f"Correct! You guessed it in {self.trial} attempts!",
            )
            self.new_game()

    def new_game(self):
        self.hid_number = random.randint(1, 20)
        self.trial = 0
        self.entry.delete(0, tk.END)
        messagebox.showinfo("New Game", "A new game has started!")

# Running the program
if __name__ == "__main__":
    root = tk.Tk()
    game = NoguessGame(root)  
    root.mainloop()