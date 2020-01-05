import random
def viewBackToFront(board):
    for i in range(4):
        print()
        print("level " + str(i+1))
        for j in range(4):
            print()
            if(j!=0):
                for l in range(8):
                    print("-",end = '')
            print()
            for k in range(4):
                if(board[i][3-j][k]==3):
                    if(k!=3):
                        print("x",end = '|')
                    else:
                        print("x",end = '')
                elif(board[i][3-j][k]==5):
                    if(k!=3):
                        print("o",end = '|')
                    else:
                        print("o",end = '')
                else:
                    if(k!=3):
                        print(" ",end = '|')
                    else:
                        print(" ",end = '')
def viewLeftToRight(board):
    for i in range(4):
        print()
        print("level " + str(i+1))
        for j in range(4):
            print()
            if(j!=0):
                for l in range(8):
                    print("-",end = '')
            print()
            for k in range(4):
                if(board[3-k][3-j][i]==3):
                    if(k!=3):
                        print("x",end = '|')
                    else:
                        print("x",end = '')
                elif(board[3-k][3-j][i]==5):
                    if(k!=3):
                        print("o",end = '|')
                    else:
                        print("o",end = '')
                else:
                    if(k!=3):
                        print(" ",end = '|')
                    else:
                        print(" ",end = '')
def viewTopToBottom(board):
    for i in range(4):
        print()
        print("level " + str(i+1))
        for j in range(4):
            print()
            if(j!=0):
                for l in range(8):
                    print("-",end = '')
            print()
            for k in range(4):
                if(board[3-j][3-i][k]==3):
                    if(k!=3):
                        print("x",end = '|')
                    else:
                        print("x",end = '')
                elif(board[3-j][3-i][k]==5):
                    if(k!=3):
                        print("o",end = '|')
                    else:
                        print("o",end = '')
                else:
                    if(k!=3):
                        print(" ",end = '|')
                    else:
                        print(" ",end = '')
if __name__ == "__main__":
    board = []
    for i in range(4):
        board.append([])
        for k in range(4):
            board[i].append([])
            for j in range(4):
                board[i][k].append(random.choice([1,3,5]))
    viewBackToFront(board)
    #viewLeftToRight(board)
    viewTopToBottom(board)
            
            