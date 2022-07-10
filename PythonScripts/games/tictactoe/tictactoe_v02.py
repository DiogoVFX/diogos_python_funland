def create_grid():
    grid_list = []
    for letter in letters:
        for number in numbers:
            grid_list.append(letter+number)
    grid_dict = {i:i for i in grid_list}
    return grid_dict, grid_list

def draw_grid(grid_dict, grid_list):
    print(f'\n{grid_dict[grid_list[0]]}|{grid_dict[grid_list[1]]}|{grid_dict[grid_list[2]]}')
    print('--+--+--')
    print(f'{grid_dict[grid_list[3]]}|{grid_dict[grid_list[4]]}|{grid_dict[grid_list[5]]}')
    print('--+--+--')
    print(f'{grid_dict[grid_list[6]]}|{grid_dict[grid_list[7]]}|{grid_dict[grid_list[8]]}')

def place_input(player_input,grid_dict, which_player):
    if which_player == 1:
        play = 'O '
    else:
        play = 'X '
    grid_dict[player_input] = play
    return grid_dict

def check_win(grid_dict, player):
    plays = ['O ','X '][player-1]
    for space in grid_dict:
        space_letter, space_number = space[0],space[1]
        letter_idx = letters.index(space_letter)
        number_idx = numbers.index(space_number)
        if space_letter == 'A':
            if space_number == '1':
                if grid_dict[letters[letter_idx]+numbers[number_idx]] in plays and grid_dict[letters[letter_idx+1]+numbers[number_idx+1]] in plays and grid_dict[letters[letter_idx+2]+numbers[number_idx+2]] in plays:
                    return True
            if space_number == '3':
                if grid_dict[letters[letter_idx]+numbers[number_idx]] in plays and grid_dict[letters[letter_idx+1]+numbers[number_idx-1]] in plays and grid_dict[letters[letter_idx+2]+numbers[number_idx-2]] in plays:
                    return True
            if space_number in numbers:
                if grid_dict[letters[letter_idx]+numbers[number_idx]] in plays and grid_dict[letters[letter_idx+1]+numbers[number_idx]] in plays and grid_dict[letters[letter_idx+2]+numbers[number_idx]] in plays:
                    return True
        if space_number == '1':
            if grid_dict[letters[letter_idx]+numbers[number_idx]] in plays and grid_dict[letters[letter_idx]+numbers[number_idx+1]] in plays and grid_dict[letters[letter_idx]+numbers[number_idx+2]] in plays:
                    return True
    return False


letters = ['A','B','C']
numbers = ['1','2','3']
grid_dict, grid_list = create_grid()

win = False
which_player = 1
while not win:
    draw_grid(grid_dict,grid_list)
    player = f'Player{which_player}'
    player_input = input(f"\nIt is {player}'s turn:")
    grid_dict = place_input(player_input, grid_dict, which_player)

    win = check_win(grid_dict, which_player)
    if which_player == 1 and win == False:
        which_player = 2
    elif which_player == 2 and win == False:
        which_player = 1

draw_grid(grid_dict,grid_list)
print(f'\nCongratulations {player}, you have won!')