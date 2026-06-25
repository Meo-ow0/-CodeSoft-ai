import random

HUMAN_PLAYER = 'O'
AI_PLAYER = 'X'
EMPTY = ' '

WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board(board):
    print('\n')
    for row in range(3):
        print(' | '.join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print('---------')
    print('\n')


def is_board_full(board):
    return all(cell != EMPTY for cell in board)


def get_empty_cells(board):
    return [index for index, cell in enumerate(board) if cell == EMPTY]


def check_winner(board, player):
    return any(all(board[pos] == player for pos in line) for line in WINNING_LINES)


def minimax(board, depth, is_maximizing):
    if check_winner(board, AI_PLAYER):
        return 10 - depth
    if check_winner(board, HUMAN_PLAYER):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_empty_cells(board):
            board[move] = AI_PLAYER
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_empty_cells(board):
            board[move] = HUMAN_PLAYER
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    best_score = -float('inf')
    best_moves = []

    for move in get_empty_cells(board):
        board[move] = AI_PLAYER
        score = minimax(board, 0, False)
        board[move] = EMPTY

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

    return random.choice(best_moves) if best_moves else None


def human_move(board):
    while True:
        try:
            choice = int(input('Enter your move (1-9): ').strip()) - 1
        except ValueError:
            print('Please enter a number between 1 and 9.')
            continue

        if choice < 0 or choice > 8:
            print('Move must be between 1 and 9.')
            continue
        if board[choice] != EMPTY:
            print('That cell is already taken. Choose another one.')
            continue

        board[choice] = HUMAN_PLAYER
        break


def play():
    board = [EMPTY] * 9
    print('Tic-Tac-Toe: You are O, AI is X')
    print('Cells are numbered 1-9 starting at the top-left.')

    current_player = HUMAN_PLAYER

    while True:
        print_board(board)

        if current_player == HUMAN_PLAYER:
            human_move(board)
        else:
            move = get_best_move(board)
            if move is None:
                break
            board[move] = AI_PLAYER
            print(f'AI chooses cell {move + 1}.')

        if check_winner(board, current_player):
            print_board(board)
            winner = 'You' if current_player == HUMAN_PLAYER else 'AI'
            print(f'{winner} win!')
            break

        if is_board_full(board):
            print_board(board)
            print('It\'s a tie!')
            break

        current_player = AI_PLAYER if current_player == HUMAN_PLAYER else HUMAN_PLAYER


if __name__ == '__main__':
    play()
