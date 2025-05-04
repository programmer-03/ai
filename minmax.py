def print_board(b):
    for i in range(0, 9, 3):
        print(b[i:i+3])

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i, j, k in wins:
        if b[i] == b[j] == b[k] and b[i] != ' ':
            return b[i]
    return None if ' ' in b else 'D' 

def minimax(b, is_max):
    winner = check_winner(b)
    if winner == 'X': return 1
    if winner == 'O': return -1
    if winner == 'D': return 0

    scores = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if is_max else 'O'
            scores.append(minimax(b, not is_max))
            b[i] = ' '
    return max(scores) if is_max else min(scores)

def best_move(b):
    best = -2
    move = -1
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X'
            score = minimax(b, False)
            b[i] = ' '
            if score > best:
                best = score
                move = i
    return move

board = [" "] * 9
while True:
    ai = best_move(board)
    board[ai] = 'X'
    print_board(board)
    if check_winner(board):
        break
    pos = int(input("Enter O's move (0-8): "))
    if board[pos] != ' ':
        print("Invalid move."); continue
    board[pos] = 'O'
    if check_winner(board):
        break

w = check_winner(board)
print("Winner:", w if w != 'D' else "Draw")
