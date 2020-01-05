import view
def checkgrid(grid):
    rprod = 1
    cprod = 1
    dprod = 1
    odprod = 1
    for i in range(4):
        rprod = 1
        cprod = 1
        for j in range(4):
            rprod*=grid[i][j]
            cprod*=grid[j][i]
        if(rprod == 81 or cprod == 81):
            return 3
        elif(cprod == 625 or cprod == 625):
            return 5
        dprod *=grid[i][i]
        odprod*=grid[3-i][i]
    if(dprod == 81 or odprod == 81):
        return 3
    elif(dprod == 625 or odprod == 625):
        return 5
    return 0
    
def isComplete(board):
    bgrid = []
    for i in range(4):
        bgrid.append([])
        for j in range(4):
            bgrid[i].append(board[j][i])
    lgrid = []
    for i in range(4):
        lgrid.append([])
        for j in range(4):
            lgrid[i].append([])
            for k in range(4):
                lgrid[i][j].append(board[k][j][i])
    for i in range(4):
        val = max(checkgrid(board[i]),checkgrid(bgrid[i]),checkgrid(lgrid[i]))
        if(val!=0):
            return val
    dprod = 1
    odprod = 1
    rdprod = 1
    rodprod = 1
    for i in range(4):
        dprod*=board[i][i][i]
        odprod*=board[i][3-i][i]
        rdprod*=board[3-i][i][i]
        rodprod*=board[3-i][3-i][i]
    if(dprod == 81 or odprod == 81 or rdprod == 81 or rodprod == 81):
        return 3
    if(dprod == 625 or odprod == 625 or rdprod == 625 or rodprod == 625):
        return 5
    return 0

def hasSpace(board):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if(board[i][j][k]==1):
                    return 1
    return 0


if __name__ == "__main__":
    board = []
    for i in range(4):
        board.append([])
        for k in range(4):
            board[i].append([])
            for j in range(4):
                board[i][k].append(1)
        #board[0][i][i] = 5
    board[1][2][3] = 3

            
    print(isComplete(board))
    view.viewBackToFront(board)
    #view.viewLeftToRight(board)
    #view.viewTopToBottom(board)
    
    

