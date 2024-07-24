from tkinter import Tk, Button, Label
import tkinter.messagebox as msgbox
import random

def on_click(row: int, column: int):
    button = buttons[row][column]
    if button.cget("text") and button.cget("text") != "":
        return
    
    global player, current_lines_length
    
    player = int(not player)
    current_lines_length += 1

    button.config(text=symbols[player])
    winner = get_winner()

    if winner is not None:
        title = "Win!"
        msg = f"{players[winner]} win the TicTacToe"
        scores[winner] += 1
    elif current_lines_length >= 9:
        title = "Tie!"
        msg = f"No winners for this game, replay?"
        scores[-1] += 1 # Tie
    else:
        return
    
    display_scores()
    msgbox.showinfo(title=title, message=msg)
    reset()

def reset(ask: bool = False):
    global current_lines_length, player

    if current_lines_length == 0:
        return
    
    if ask and not msgbox.askyesno(title='Restart the game', message='Ok?'):
        return

    current_lines_length = 0
    player = random.randint(0, 1)
    
    for rows in buttons:
        for button in rows:
            button.config(text="")

def get_winner():
    lines = get_lines()

    for line in lines:
        if line[0] == line[1] == line[2] and line[0]:
            return symbols.index(line[0])
    return None

def get_lines():
    lines = [
        [buttons[row][column].cget("text") for column in range(3)] for row in range(3)
    ] + [
        [buttons[row][column].cget("text") for row in range(3)] for column in range(3)
    ] + [
        [buttons[row][row].cget("text") for row in range(3)],
        [buttons[row][2-row].cget("text") for row in range(3)]
    ]

    return lines

def display_scores():
    global scores_label
    msg = f"""
X: {scores[0]}
O: {scores[1]}
Tie's: {scores[-1]}
"""
    if scores_label is None:
        scores_label = Label(window, text=msg, font=("Arial", 50))
        scores_label.grid(row=3, column=0, columnspan=3)
    else:
        scores_label.config(text=msg)

window = Tk()
window.title("TicTacToe")
window.minsize(500, 500)

# Constants
__font__ = "black"
__back__ = "white"
symbols = ["X", "O"] #["\u274C", "\u2B55"] 
players = ["X", "O"]

# Variables and storage
player = random.randint(0, 1)
buttons = [[], [], []]
scores = [0, 0, 0] #X win's count, O win's count, tie's count
current_lines_length = 0
scores_label = None

# Buttons (for the rows and columns)
for i in range(9):
    row, col = divmod(i, 3)
    button = Button(
        window,
        command=lambda r=row, c=col: on_click(r, c),
        font=("Arial", 40),
        bg=__back__,
        fg=__font__,
        width=5, 
        height=2
    )
    button.grid(row=row, column=col)
    buttons[row].append(button)

display_scores()
Button(window, text="Restart", command=lambda: reset(ask=True), font=("Arial", 20)).grid(row=4, column=2)

window.mainloop()
