import random
import tkinter as tk
from tkinter import messagebox

# Global variables to store the score
playerScore = 0
computerScore = 0
roundsPlayed = 1

# Global variables for matches won
playerOverallScore = 0
computerOverallScore = 0

# Function to generate the computer's choice
def getComputerChoice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

# Function to handle the user's choice and gets the computers choice
def handleChoice(playerChoice):
    global playerScore
    global computerScore
    global roundsPlayed

    global playerOverallScore
    global computerOverallScore

    computerChoice = getComputerChoice() # Stores results of getComputerChoice

    winner = determineWinner(playerChoice, computerChoice) # Stores results of the determineWinner function
    # Adds to round score of player of computer
    if winner == "Player":
        playerScore += 1
    elif winner == "Computer":
        computerScore += 1

    # Does not count rounds that ends in Tie
    if winner != "Tie":
        roundsPlayed += 1

    roundText.set(f"Round: {roundsPlayed}")    

    # Determines if player or computer have won yet and adds to the overall score of the winner
    if playerScore == 2 or computerScore == 2:
        if playerScore > computerScore:
            overall_winner = "Player"
            playerOverallScore += 1
        elif computerScore > playerScore:
            overall_winner = "Computer"
            computerOverallScore += 1

        updateScoreBoard()
        disableButtons()
        roundLabel.grid_remove()

    # Create a new Toplevel window for the result
    resultWindow = tk.Toplevel(root)
    resultWindow.title("Result")

    # Create image labels for player's and computer's choices
    playerImg = globals()[playerChoice.lower() + "Img"]
    computerImg = globals()[computerChoice.lower() + "Img"]

    playerLabel = tk.Label(resultWindow, image=playerImg)
    computerLabel = tk.Label(resultWindow, image=computerImg)

    # Create text labels for player's and computer's choices
    playerChoiceLabel = tk.Label(resultWindow, text=f"Player chose: {playerChoice}")
    computerChoiceLabel = tk.Label(resultWindow, text=f"Computer chose: {computerChoice}")

    # Create winnerLabel with different text depending on the result
    if winner == "Tie":
        winnerLabel = tk.Label(resultWindow, text="It's a tie! The round doesn't count.")
    else:
        winnerLabel = tk.Label(resultWindow, text=f"{winner} wins this round!")

    # Create an exit button for the result window
    exitResultButton = tk.Button(resultWindow, text="Exit", command=resultWindow.destroy)

    # Grid layout for the result window
    playerLabel.grid(row=0, column=0, padx=20, pady=10)
    computerLabel.grid(row=0, column=1, padx=20, pady=10)
    playerChoiceLabel.grid(row=1, column=0, padx=20, pady=10)
    computerChoiceLabel.grid(row=1, column=1, padx=20, pady=10)
    winnerLabel.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
    exitResultButton.grid(row=3, column=0, columnspan=2, pady=10)

    # Make the result window modal to prevent interaction with the main window
    resultWindow.transient(root)
    resultWindow.grab_set()
    root.wait_window(resultWindow)

    # Displays Final results after round results
    if playerScore == 2 or computerScore == 2:
        messagebox.showinfo("Final Result", f"Final Score: \nComputer: {computerScore}\nPlayer: {playerScore}\n{overall_winner} wins!")

            
# Function to determine the winner of the game
def determineWinner(playerChoice, computerChoice):
    # checks choices made against eachother 
    if playerChoice == computerChoice:
        return "Tie"
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
    global playerScore
    global computerScore
    global roundsPlayed

    playerScore = 0
    computerScore = 0
    roundsPlayed = 1
    roundText.set(f"Round: {roundsPlayed}")
    enableButtons()

    roundLabel.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

# Function to disable buttons
def disableButtons():
    rockButton.config(state=tk.DISABLED)
    paperButton.config(state=tk.DISABLED)
    scissorsButton.config(state=tk.DISABLED)

# Function to enable buttons
def enableButtons():
    rockButton.config(state=tk.NORMAL)
    paperButton.config(state=tk.NORMAL)
    scissorsButton.config(state=tk.NORMAL)

# Function to update the overall score board
def updateScoreBoard():
    scoreBoardText.set(f"Matches Won:\nPlayer: {playerOverallScore}\nComputer: {computerOverallScore}")

# Function to quit the application
def quit():
    root.destroy()

# Function to display the rules of the game
def Rules():
    howToPlay = "Each player chooses either rock, paper or scissors. \n\nThe rules are: \n\nRock beats Scissors \nScissors beats Paper \nPaper beats Rock\
    \n\nThe winner is the one who wins the best of three rounds (ties don't count). Good Luck!"

    messagebox.showinfo("How to Play", howToPlay)

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create the images, labels, and choice buttons
rockImg = tk.PhotoImage(file="rock.png")
paperImg = tk.PhotoImage(file="paper.png")
scissorsImg = tk.PhotoImage(file="scissors.png")

rockButton = tk.Button(root, image=rockImg, command=lambda: handleChoice("Rock"))
paperButton = tk.Button(root, image=paperImg, command=lambda: handleChoice("Paper"))
scissorsButton = tk.Button(root, image=scissorsImg, command=lambda: handleChoice("Scissors"))

# Create the reset and exit buttons
resetButton = tk.Button(root, text="Reset", command=reset)
exitButton = tk.Button(root, text="Exit", command=quit)

# Create the How to Play button
howToPlayButton = tk.Button(root, text="How to Play", command=Rules)

# Create a label to prompt user input
promptLabel = tk.Label(root, text="Try to defeat the computer in a best of 3 match. Please select Rock, Paper, or Scissors")

# Create string variable to store round number and label to display
roundText = tk.StringVar() # Stores round number
roundText.set(f"Round: {roundsPlayed}")
roundLabel = tk.Label(root, textvariable=roundText)

# Create a StringVar to store score board and Label for the score board
scoreBoardText = tk.StringVar()# Stores text for score board
updateScoreBoard()
scoreBoardLabel = tk.Label(root, textvariable=scoreBoardText)

# Uses grid to build the game window with buttons and labels

# Labels
promptLabel.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
roundLabel.grid(row=1, column=0, columnspan=3, padx=20, pady=10)
scoreBoardLabel.grid(row=1, column=2, columnspan=1, padx=20, pady=10)

# Buttons
rockButton.grid(row=2, column=0, padx=20, pady=10)
paperButton.grid(row=2, column=1, padx=20, pady=10)
scissorsButton.grid(row=2, column=2, padx=20, pady=10)
resetButton.grid(row=3, column=0, pady=10)
exitButton.grid(row=3, column=2, pady=10)
howToPlayButton.grid(row=3, column=1, pady=10)

root.mainloop()

