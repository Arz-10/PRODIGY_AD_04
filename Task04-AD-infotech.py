import tkinter as tk
from tkinter import messagebox

# Function to initialize/reset the game
def reset_game():
    global board
    board = [[None, None, None] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="light gray", state="normal")
    global turn
    turn = "X"

# Function to handle button click events
def button_click(row, col):
    global turn
    if board[row][col] is None:
        buttons[row][col].config(text=turn, bg="light blue" if turn == "X" else "light green")
        board[row][col] = turn
        if check_winner(turn):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {turn} wins!")
            for r in range(3):
                for c in range(3):
                    buttons[r][c].config(state="disabled")
        elif all(board[r][c] is not None for r in range(3) for c in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        else:
            turn = "O" if turn == "X" else "X"

# Function to check for a winner
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#4682B4")

# Initialize the game state
turn = "X"
board = [[None, None, None] for _ in range(3)]

# Create buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=('Arial', 20), width=5, height=2,
                                      command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

# Create reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 16), command=reset_game, bg="light gray")
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Start the main loop
root.mainloop()

