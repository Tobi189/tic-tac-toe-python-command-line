turn = 'x'
board = [None for _ in range(9)]
game_over = False
move = None
winner = False
def draw_board():
    for i in range(3):
        row = []
        for j in range(3):
            cell = board[i*3 + j]
            row.append(cell if cell is not None else str(i*3 + j + 1))
        print(' | '.join(row))
        if i != 2:
            print('---------')

def make_move():
    global turn
    valid = False
    while not valid:
        print(f"{turn}'s turn")
        move = input('Please input number between 1-9: ').strip()
        if not (move.isdigit() and 1 <= int(move) <= 9):
            print('Invalid input. Please enter a number between 1 and 9.')
            continue
        idx = int(move) - 1
        if board[idx] is not None:
            print('Cell already taken. Choose another one.')
            continue
        board[idx] = turn
        valid = True
    draw_board()
    # Switch turn
    turn = 'o' if turn == 'x' else 'x'

def choose_first_player():
    global turn
    print('Choose first player: ')
    print('1 - x')
    print('2 - o')
    choice = input('Please input 1 or 2: ').strip()
    while choice not in ('1', '2'):
        print('Please input 1 or 2 to choose the first player: ')
        choice = input('Your input here: ').strip()
    turn = 'x' if choice == '1' else 'o'

def check_winner():
    global board
    winner = False
    for i in range(3):
        if board[3*i] and (board[3*i] == board[3*i+1] and board[3*i] == board[3*i+2]):
            print(f'{board[3*i]} is the winner!')
            winner = True
        if board[i] and (board[i] == board[i+3] and board[i] == board[i+6]):
            print(f'{board[i]} is the winner!')
            winner = True
    if board[0] and (board[0] == board[4] and board[0] == board[8]):
        print(f'{board[0]} is the winner!')
        winner = True
    if board[2] and (board[2] == board[4] and board[2] == board[6]):
        print(f'{board[2]} is the winner!')
        winner = True

    if winner:
        while True:
            answer = input('Do you want to play again y/n: ').strip()
            if len(answer) != 1 or (answer.lower() != 'n' and answer.lower() != 'y'):
                print('Please enter valid input')
                continue
            if answer.lower() == 'n':
                exit()
            else:
                board = [None for _ in range(9)]
                game_loop()
            break
    elif all(cell is not None for cell in board):
        print("It's a draw!")
        while True:
            answer = input('Do you want to play again y/n: ').strip()
            if len(answer) != 1 or (answer.lower() != 'n' and answer.lower() != 'y'):
                print('Please enter valid input')
                continue
            if answer.lower() == 'n':
                exit()
            else:
                board = [None for _ in range(9)]
                game_loop()
            break



# Example game loop (you can expand this with win/draw detection)

def game_loop():
    choose_first_player()
    draw_board()
    for _ in range(9):
        make_move()
        check_winner()


game_loop()


