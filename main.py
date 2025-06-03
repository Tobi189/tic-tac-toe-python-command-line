


turn = 'x'
board = [None for _ in range(9)]
game_over = False

def print_board():
    print('\n')
    for i in range(3):
        print(' | '.join([str(board[i * 3]) if board[i * 3] is not None else ' ' for i in range(3)])) 
        if i == 2:
            continue
        print('---------')

def check_winner():
    for i in range(3):
        if (board[i*3] == 'x' and board[(i+1)*3] == 'x' and board[(i+2)*3] == 'x') or (board[i] == 'x' and board[i+1] == 'x' and board[i+2] == 'x'):
            return 'x'
        elif(board[i*3] == 'o' and board[(i+1)*3] == 'o' and board[(i+2)*3] == 'o') or (board[i] == 'o' and board[i+1] == 'o' and board[i+2] == 'o'):
            return 'o'

def reset_game():
    turn = 'x'
    board = [None for _ in range(9)]
    game_over = False

