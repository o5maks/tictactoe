from tkinter import Tk, Button, Label
import tkinter.messagebox as msgbox

def onClick(row, column):
    button = buttons[row][column]
    if button.cget("text") and button.cget("text") != "":
        return
    
    global player
    global current_lines_length
    player = int(not player)
    current_lines_length += 1

    button.config(text=symbols[player])
    winner = getWinner()

    if winner:
        msg = f"{winner} win the TicTacToe"
        msgbox.showinfo(message=msg)
    elif current_lines_length >= 9:
        msg = f"No winners for this game, replay?"
        msgbox.showinfo(message=msg)
    else:
        return
    
    current_lines_length = 0
    for rows in buttons:
        for column in rows:
            column.config(text="")

def getWinner():
    lines = getLines()

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != "":
            return line[0]

    return None

def getLines():
    lines = [
        [buttons[row][column].cget("text") for column in range(3)] for row in range(3)
    ] + [
        [buttons[row][column].cget("text") for row in range(3)] for column in range(3)
    ] + [
        [buttons[row][row].cget("text") for row in range(3)],
        [buttons[row][2-row].cget("text") for row in range(3)]
    ]

    return lines

window = Tk()
window.title("TicTacToe")
window.minsize(500, 500)

# Constants
__font__ = "black"
__back__ = "white"
symbols = ["\u274C", "\u2B55"] 
players = ["X", "O"]

# Variables and storage
player = 0
buttons = [[], [], []]
current_lines_length = 0

# Buttons (for the rows and columns)
for i in range(9):
    row, col = divmod(i, 3)
    button = Button(
        window,
        command=lambda r=row, c=col: onClick(r, c),
        font=("Arial", 40),
        bg=__back__,
        fg=__font__,
        width=5, 
        height=2
    )
    button.grid(row=row, column=col)
    buttons[row].append(button)

window.mainloop()