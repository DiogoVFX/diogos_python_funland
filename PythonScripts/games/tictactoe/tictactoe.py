# A script that lets two people play tictactoe

# Player Variables
p1_choices = []
p2_choices = []
p1_win = False
p2_win = False

# Functions
def check_player_win(choices):
    win_combos = [[1,2,3],[4,5,6],[7,8,9], # Line by line
                  [1,4,7],[2,5,8],[3,6,9], # Top to bottom
                  [1,5,9],[3,5,7]] # Diagonal
    choices.sort()
    for count, combo in enumerate(win_combos):
        for num in choices:
            if num == combo[0]:
                try:
                    combo.pop(0)
                    win_combos[count] = combo
                except ValueError:
                    pass
            else:
                pass
    for combo in win_combos:
        if not combo:
            return True
        else:
            pass
    return False

def check_input_valid(player):
    global p1_choices, p2_choices
    if player == 'X':
        player = 'Player1'
    else:
        player = 'Player2'
    player_in = int(input(f'{player} choose your spot: '))
    while player_in in p1_choices or player_in in p2_choices:
        try:
            player_in = int(input(f'{player} choose your spot: '))
            break
        except ValueError:
            break
    if player == 'Player1':
        p1_choices.append(player_in)
    else:
        p2_choices.append(player_in)
    return player_in



# ask player1 if they want to be x or o 
p1_role, p2_role = ('X','O')
print("Hi welcome to tic tac toe!\nPlayer1 you are 'X' and Player2 you are 'O'")

# play the game
board = '\n   1|2|3\n   -+-+-\n   4|5|6\n   -+-+-\n   7|8|9\n'
print(board)

while not p2_win:
    p1_input = check_input_valid(p1_role)
    p1_choices.append(p1_input)
    board = board.replace(str(p1_input),p1_role)
    print(board)
    # Check if p1 wins
    p1_win = check_player_win(p1_choices)
    if p1_win == True:
        break
    p2_input = check_input_valid(p2_role)
    p2_choices.append(int(p2_input))
    board = board.replace(str(p2_input),p2_role)
    print(board)
    p2_win = check_player_win(p2_choices)

# ask if they want to replay