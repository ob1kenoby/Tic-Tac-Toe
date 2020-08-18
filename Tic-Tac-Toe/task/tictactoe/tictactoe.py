# write your code here
def show_field():
    print('---------')
    for row in field:
        print(f'| {" ".join(row)} |')
    print('---------')


def determine_winner(spot):
    global game_is_on
    if spot == 'X':
        print("X wins")
        game_is_on = False
    elif spot == 'O':
        print('O wins')
        game_is_on = False


field = [[' ' for i in range(3)] for j in range(3)]
show_field()

game_is_on = True
step = 'X'
step_counter = 0

while game_is_on:
    incorrect_input = True
    while incorrect_input:
        incorrect_input = False
        move = input('Enter the coordinates: ').split()
        if len(move) != 2:
            print("You should enter two digits!")
            incorrect_input = True
            continue
        for i in range(2):
            if move[i].isdigit():
                move[i] = int(move[i]) - 1  # convert 1-3 to 0-2 for index convenience
                if move[i] not in range(3):  # to check if the input is in the field range 1-3
                    print("Coordinates should be from 1 to 3!")
                    incorrect_input = True
                    break
            else:
                print("You should enter numbers!")
                incorrect_input = True
                break
        if incorrect_input:
            continue
        if field[2 - move[1]][move[0]] != ' ':
            print("This cell is occupied! Choose another one!")
            incorrect_input = True

    field[2 - move[1]][move[0]] = step
    show_field()

    for i in range(len(field)):
        if field[i][0] == field[i][1] == field[i][2]:
            determine_winner(field[i][0])
        if field[0][i] == field[1][i] == field[2][i]:
            determine_winner(field[0][i])

    if field[0][0] == field[1][1] == field[2][2]:
        determine_winner(field[0][0])
    if field[0][2] == field[1][1] == field[2][0]:
        determine_winner(field[0][2])

    if game_is_on and step_counter >= 8:
        game_is_on = False
        print("Draw")

    if step == 'X':
        step = 'O'
    else:
        step = 'X'
    step_counter += 1
