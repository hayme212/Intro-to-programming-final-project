import random
import tkinter as tk
from tkinter import messagebox


# Function to generate the computer's choice
def getComputerChoice():
    choices = ["Rock", "Paper", "Scissors"] #List of available choices for computer input
    return random.choice(choices)

# Function to handle the user's choice and gets the computers choice
def handleChoice(playerChoice):
    computerChoice = getComputerChoice()
    winner = determineWinner(playerChoice, computerChoice)
    messagebox.showinfo("Result", f"Computer chose: {computerChoice}\nPlayer chose: {playerChoice}\n{winner} wins!")

# Function to determine the winner of the game
def determineWinner(playerChoice, computerChoice):
    # If statements compare user slection with computer choice
    if playerChoice == computerChoice:
        return "No one"
    elif playerChoice == "Rock":
        if computerChoice == "Paper":
            return "Computer"
        else:
            return "Player"
    elif playerChoice == "Paper":
        if computerChoice == "Scissors":
            return "Computer"
        else:
            return "Player"
    elif playerChoice == "Scissors":
        if computerChoice == "Rock":
            return "Computer"
        else:
            return "Player"

# Function to reset the game
def reset():
    resultText.set("")


# Function to quit the application
def quit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create the images, labels, and choice buttons
rockImg = tk.PhotoImage(file="rock.png") # stores image file
paperImg = tk.PhotoImage(file="paper.png") # stores image file
scissorsImg = tk.PhotoImage(file="scissors.png") # stores image file

rockButton = tk.Button(root, image=rockImg, command=lambda: handleChoice("Rock")) # displays image on button and assigns "Rock" to the function handleChoice
paperButton = tk.Button(root, image=paperImg, command=lambda: handleChoice("Paper")) #displays image on button and assigns "Rock" to the function handleChoice
scissorsButton = tk.Button(root, image=scissorsImg, command=lambda: handleChoice("Scissors")) #displays image on button and assigns "Rock" to the function handleChoice

resultText = tk.StringVar() #Tkinter string variable to be used within a messagebox to display the results
resultLabel = tk.Label(root, textvariable=resultText)


# Create the reset and exit buttons
resetButton = tk.Button(root, text="Reset", command=reset)
exitButton = tk.Button(root, text="Exit", command=quit)

# Create a label to prompt user input
promptLabel = tk.Label(root, text="Please select Rock, Paper, or Scissors")

# Uses grid to build the game window with buttons and labels
promptLabel.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
rockButton.grid(row=1, column=0, padx=20, pady=10)
paperButton.grid(row=1, column=1, padx=20, pady=10)
scissorsButton.grid(row=1, column=2, padx=20, pady=10)
resultLabel.grid(row=2, column=0, columnspan=3, padx=20, pady=10)
resetButton.grid(row=3, column=0, pady=10)
exitButton.grid(row=3, column=2, pady=10)

root.mainloop()
