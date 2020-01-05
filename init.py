import view
def init_board(board):
    for i in range(4):
        board.append([])
        for j in range(4):
            board[i].append([])
            for k in range(4):
                board[i][j].append(1)
if __name__ == "__main__":
    board = []
    init_board(board)
    view.viewBackToFront(board)
    board[3][3][3] = 3
    board[3][3][0] = 5
    board[3][0][3] = 3
    view.viewBackToFront(board)
    view.viewLeftToRight(board)
    view.viewTopToBottom(board)

