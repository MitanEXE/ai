import tkinter as tk
import tkinter.messagebox

# Constants
PLAYER_1_SYMBOL = 'X'
PLAYER_2_SYMBOL = 'O'
PLAYER_1_COLOR = "skyblue"
PLAYER_2_COLOR = "#e8956f"

# Initialize main window
window = tk.Tk()
window.title('Tic Tac Toe')

# Main frame
frame = tk.Frame(master=window)
frame.pack(pady=10)

label = tk.Label(master=frame, text="Tic Tac Toe", font=("Arial", 15))
label.pack()

# Tic Tac Toe board
frame1 = tk.Frame(master=window, borderwidth=2, relief=tk.SUNKEN, bg='#dadec3')
frame1.pack(padx=10, pady=10)

buttons = []
for i in range(9):
    button = tk.Button(master=frame1, text='', width=10, height=5, bg='white', command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(button)

# Player info and control frame
frame2 = tk.Frame(master=window, border=2, relief=tk.SUNKEN, bg='#dadec3')
frame2.pack()

label1 = tk.Label(master=frame2, text="Player 1 --> X\nPlayer 2 --> O", width=10)
label1.grid(row=0, column=0, padx=5)

button_restart = tk.Button(master=frame2, text="Restart", width=10, height=3, relief=tk.GROOVE, command=lambda: restart_game())
button_restart.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(master=frame2, text='Player-1 Turn', bg=PLAYER_1_COLOR, width=10, height=3, relief=tk.SUNKEN)
label2.grid(row=0, column=2, padx=5)

# Game state variables
current_player = PLAYER_1_SYMBOL
turn_count = 0

def disable_buttons():
    for button in buttons:
        button['state'] = tk.DISABLED

def restart_game():
    global current_player, turn_count
    current_player = PLAYER_1_SYMBOL
    turn_count = 0
    label2['bg'] = PLAYER_1_COLOR
    label2['text'] = 'Player-1 Turn'
    for button in buttons:
        button['text'] = ''
        button['bg'] = 'white'
        button['state'] = tk.NORMAL

def check_winner():
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for (a, b, c) in win_conditions:
        if buttons[a]['text'] == buttons[b]['text'] == buttons[c]['text'] != '':
            return buttons[a]['text']
    return None

def button_click(index):
    global current_player, turn_count
    if buttons[index]['text'] == '':
        buttons[index]['text'] = current_player
        buttons[index]['bg'] = PLAYER_1_COLOR if current_player == PLAYER_1_SYMBOL else PLAYER_2_COLOR
        turn_count += 1
        winner = check_winner()
        if winner:
            disable_buttons()
            tk.messagebox.showinfo("Tic Tac Toe", f"Winner is player {1 if winner == PLAYER_1_SYMBOL else 2}")
        elif turn_count == 9:
            disable_buttons()
            tk.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")
        else:
            current_player = PLAYER_2_SYMBOL if current_player == PLAYER_1_SYMBOL else PLAYER_1_SYMBOL
            label2['bg'] = PLAYER_1_COLOR if current_player == PLAYER_1_SYMBOL else PLAYER_2_COLOR
            label2['text'] = f'Player-{1 if current_player == PLAYER_1_SYMBOL else 2} Turn'

window.mainloop()
