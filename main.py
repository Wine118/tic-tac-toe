import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

def make_move(row, col):
    global current_player
    if game[row][col] == '':
        game[row][col] = current_player        
        buttons[row][col].configure(text=current_player)
        if check_winner():
            messagebox.showinfo("Game Over", f"The winner is {current_player}")
            reset_game()
        elif all(all(cell != '' for cell in row) for row in game):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == 'X' else "X"
            label.configure(text=f"{current_player}'s Turn")

def check_winner():
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != '':
            return True
        if game[0][i] == game[1][i] == game[2][i] != '':
            return True
    if game[0][0] == game[1][1] == game[2][2] != '':
        return True
    if game[0][2] == game[1][1] == game[2][0] != '':
        return True
    return False

def reset_game():
    global game, current_player
    game = [['', '', ''] for _ in range(3)]
    current_player = 'X'
    for row in buttons:
        for button in row:
            button.configure(text='')
    label.configure(text="Tic-Tac-Toe")

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")
style = Style(theme="flatly")

# Set window size and center it on the screen
window.geometry('400x450')
window.eval('tk::PlaceWindow . center')

# Change the background color
window.configure(bg='#f0f0f0')

# Configure the main window's grid to make the frame expandable
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create a frame to center the label and buttons
frame = tk.Frame(window, bg='#f0f0f0')
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Configure the frame's grid to be responsive
frame.grid_rowconfigure(0, weight=1)
for i in range(3):
    frame.grid_rowconfigure(i+1, weight=1)
    frame.grid_columnconfigure(i, weight=1)

# Create a label above the game board
label = ttk.Label(frame, text="Tic-Tac-Toe", font=("Helvetica", 18, 'bold'), background='#f0f0f0', foreground='#333')
label.grid(row=0, column=0, columnspan=3, pady=20)

# Create a custom style for the buttons with a larger font
style.configure('TicTacToe.TButton', font=("Helvetica", 18, 'bold'))

# Create Buttons for the game board
buttons = []

for i in range(3):
    row = []
    for j in range(3):
        button = ttk.Button(frame, text='', width=6, style="TicTacToe.TButton", command=lambda i=i, j=j: make_move(i, j))
        button.grid(row=i+1, column=j, padx=10, pady=10, sticky="nsew")  # Use sticky="nsew" to center buttons
        row.append(button)
    buttons.append(row)

# Initialize the game board and the current player
game = [['', '', ''] for _ in range(3)]
current_player = 'X'

window.mainloop()
