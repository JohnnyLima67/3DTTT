from checkComplete import isComplete,hasSpace
from init import init_board
import view
import time
MAXDEPTH = 0
from progressbar import ProgressBar
def minimax(board , depth , isMax,blockOccurs):


    winner = isComplete(board)
    if winner == 3:
        if(len(blockOccurs)<1):
            blockOccurs.append(True)
        #print("reached")
        return (-66+depth)
    if winner == 5:
        if(len(blockOccurs)<1):
            blockOccurs.append(True)
        #print("reached")
        return (66-depth)
    if hasSpace(board) == 0:
        return 0
    if(depth > MAXDEPTH):
        return 0
    counter= 0
    if(isMax == 1): #check if we are trying to find optimal for maximizer
        bestVal = -1000
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if(board[i][j][k]==1):

                        board[i][j][k] = 5
                        bestVal = max(bestVal,minimax(board,depth+1,0,blockOccurs))
                        board[i][j][k] = 1
                        counter+=1
                        if(bestVal>0):
                            return bestVal
        return bestVal
    elif(isMax == 0): #check if we are trying to find optimal for maximizer
        bestVal = 1000
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if(board[i][j][k]==1):
                        board[i][j][k] = 3
                        bestVal = min(bestVal,minimax(board,depth+1,1,blockOccurs))
                        board[i][j][k] = 1
                        if(bestVal<0):
                            return bestVal
        return bestVal
def Movebest(board,isMax):
    progress = ProgressBar(64, fmt=ProgressBar.FULL)
    if(isMax==1):
        bestVal = -1000
        
        count = 0
        bestLevel = -1
        bestRow = -1
        bestCol = -1
        blockOccurs = []
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    #print(count)
                    progress()
                    if(board[i][j][k] == 1):
                        board[i][j][k]=5
                        newVal=minimax(board,0,0,blockOccurs)
                        if(newVal>bestVal):
                            bestVal = newVal
                            bestLevel = i
                            bestRow = j
                            bestCol = k
                            if(bestVal > 0):
                                break
                        elif(newVal==bestVal):
                            if i in [1,2] :
                                if j in [1,2] :
                                    if k in [1,2] :
                                        bestLevel = i
                                        bestRow = j
                                        bestCol = k
                            elif bestLevel not in [1,2]:
                                if j in [1,2] :
                                    if k in [1,2] :
                                        bestLevel = i
                                        bestRow = j
                                        bestCol = k
                                elif bestRow not in [1,2]:
                                    if k in [1,2]:
                                        bestLevel = i
                                        bestRow = j
                                        bestCol = k
                        board[i][j][k] = 1
                if(bestVal>0):
                    break
            if(bestVal>0):
                break
        print(blockOccurs)
        if(bestVal==0 and len(blockOccurs)<1):
            flag = 0
            tempd = 1
            tempod = 1
            temprd = 1
            temprod = 1
            cd = 0
            cod = 0
            crd = 0
            crod =0
            for i in range(4):
                if(board[i][i][i]!=1):
                    if(board[i][i][i]==tempd or tempd == 1):
                        tempd = board[i][i][i]
                        cd+=1
                if(board[3-i][i][i]!=1):
                    if(board[3-i][i][i]==tempod or tempod == 1):
                        tempod = board[3-i][i][i]
                        cod+=1
                if(board[i][3-i][i]!=1):
                    if(board[i][3-i][i]==temprd or temprd == 1):
                        temprd = board[i][3-i][i]
                        crd+=1
                if(board[3-i][3-i][i]!=1):
                    if(board[3-i][3-i][i]==temprod or temprod == 1):
                        temprod = board[3-i][3-i][i]
                        crod+=1
            if(cd == 2):
                for i in range(4):
                    if(board[i][i][i]==1):
                        bestLevel = i
                        bestRow = i
                        bestCol = i
                        flag = 1
                        break
            if(cod == 2 and flag!=1):
                for i in range(4):
                    if(board[3-i][i][i]==1):
                        bestLevel = 3-i
                        bestRow = i
                        bestCol = i
                        flag = 1
                        break
            if(crd == 2 and flag!=1):
                for i in range(4):
                    if(board[i][3-i][i]==1):
                        bestLevel = i
                        bestRow = 3-i
                        bestCol = i
                        flag = 1
                        break
            if(crod == 2 and flag!=1):
                for i in range(4):
                    if(board[3-i][3-i][i]==1):
                        bestLevel = 3-i
                        bestRow = 3-i
                        bestCol = i
                        flag = 1
                        break
            for i in range(4):
                if(flag==1):
                    break
                for j in range(4):
                    cr=0
                    cc=0
                    cl=0
                    tempr = 1
                    tempc = 1
                    templ = 1
                    for k in range(4):
                        if(flag==1):
                            break
                        if(board[i][j][k]!=1):
                            if(tempr==1 or board[i][j][k]==tempr):
                                tempr = board[i][j][k]
                                cr+=1 
                        if(board[i][k][j]!=1):
                            if(tempc==1 or board[i][k][j]==tempc):
                                tempc = board[i][k][j]
                                cc+=1
                        if(board[k][j][i]!=1):
                            if(templ==1 or board[k][j][i]==templ):
                                templ = board[k][j][i]
                                cl+=1
                    
                    if(cr==2):
                        for k in range(4):
                            if(board[i][j][k]==1):
                                bestLevel = i
                                bestRow = j
                                bestCol = k
                                flag = 1 
                                break
                    if(cc==2 and flag!=1):
                        for k in range(4):
                            if(board[i][k][j]==1):
                                bestLevel = i
                                bestRow = k
                                bestCol = j
                                flag = 1 
                                break
                    if(cl==2 and flag!=1):
                        for k in range(4):
                            if(board[k][j][i]==1):
                                bestLevel = k
                                bestRow = j
                                bestCol = i
                                flag = 1 
                                break
                    if(flag==1):
                        break
                if(flag==1):
                    break
        board[bestLevel][bestRow][bestCol] = 5
        #poslist.append(bestLevel)
        #poslist.append(bestRow)
        #poslist.append(bestCol)
    elif(isMax==0):
        bestVal = 1000
        bestLevel = -1
        bestRow = -1
        bestCol = -1
        for i in range(4):
            for j in range(4):
                for k in range(4):
                   # print(count)
                    progress()
                    if(board[i][j][k] == 1):
                        board[i][j][k]=3
                        newVal=minimax(board,0,1)
                        if(newVal<bestVal):
                            bestVal = newVal
                            bestLevel = i
                            bestRow = j
                            bestCol = k
                            if(bestVal<0):
                                break
                        elif(newVal==bestVal):
                            if i in [1,2] :
                                if j in [1,2] :
                                    if k in [1,2] :
                                        bestLevel = i
                                        bestRow = j
                                        bestCol = k
                            elif bestLevel not in [1,2]:
                                if j in [1,2] :
                                    if k in [1,2] :
                                        bestLevel = i
                                        bestRow = j
                                        bestCol = k
                                elif bestRow not in [1,2]:
                                    if k in [1,2]:
                                        bestLevel = i
                                        bestRow = j
                                        bestCol = k



                        board[i][j][k] = 1
                if(bestVal<0):
                    break
            if(bestVal<0):
                break
        if(bestVal==0 and len(blockOccurs)<1):
            flag = 0
            tempd = 1
            tempod = 1
            temprd = 1
            temprod = 1
            cd = 0
            cod = 0
            crd = 0
            crod =0
            for i in range(4):
                if(board[i][i][i]!=1):
                    if(board[i][i][i]==tempd or tempd == 1):
                        tempd = board[i][i][i]
                        cd+=1
                if(board[3-i][i][i]!=1):
                    if(board[3-i][i][i]==tempod or tempod == 1):
                        tempod = board[3-i][i][i]
                        cod+=1
                if(board[i][3-i][i]!=1):
                    if(board[i][3-i][i]==temprd or temprd == 1):
                        temprd = board[i][3-i][i]
                        crd+=1
                if(board[3-i][3-i][i]!=1):
                    if(board[3-i][3-i][i]==temprod or temprod == 1):
                        temprod = board[3-i][3-i][i]
                        crod+=1
            if(cd == 2):
                for i in range(4):
                    if(board[i][i][i]==1):
                        bestLevel = i
                        bestRow = i
                        bestCol = i
                        flag = 1
                        break
            if(cod == 2 and flag!=1):
                for i in range(4):
                    if(board[3-i][i][i]==1):
                        bestLevel = 3-i
                        bestRow = i
                        bestCol = i
                        flag = 1
                        break
            if(crd == 2 and flag!=1):
                for i in range(4):
                    if(board[i][3-i][i]==1):
                        bestLevel = i
                        bestRow = 3-i
                        bestCol = i
                        flag = 1
                        break
            if(crod == 2 and flag!=1):
                for i in range(4):
                    if(board[3-i][3-i][i]==1):
                        bestLevel = 3-i
                        bestRow = 3-i
                        bestCol = i
                        flag = 1
                        break
            for i in range(4):
                if(flag==1):
                    break
                for j in range(4):
                    cr=0
                    cc=0
                    cl=0
                    tempr = 1
                    tempc = 1
                    temp = 1
                    for k in range(4):
                        if(flag==1):
                            breaks
                        if(board[i][j][k]!=1):
                            if(tempr==1 or board[i][j][k]==tempr):
                                tempr = board[i][j][k]
                                cr+=1 
                        if(board[i][k][j]!=1):
                            if(tempc==1 or board[i][k][j]==tempc):
                                tempc = board[i][k][j]
                                cc+=1
                        if(board[k][j][i]!=1):
                            if(templ==1 or board[k][j][i]==templ):
                                templ = board[k][j][i]
                                cl+=1
                    
                    if(cr==2):
                        for k in range(4):
                            if(board[i][j][k]==1):
                                bestLevel = i
                                bestRow = j
                                bestCol = k
                                flag = 1 
                                break
                    if(cc==2 and flag!=1):
                        for k in range(4):
                            if(board[i][k][j]==1):
                                bestLevel = i
                                bestRow = k
                                bestCol = j
                                flag = 1 
                                break
                    if(cl==2 and flag!=1):
                        for k in range(4):
                            if(board[k][j][i]==1):
                                bestLevel = k
                                bestRow = j
                                bestCol = i
                                flag = 1 
                                break
                    if(flag==1):
                        break
                if(flag==1):
                    break
        
        board[bestLevel][bestRow][bestCol] = 3
        #poslist.append(bestLevel)
        #poslist.append(bestRow)
        #poslist.append(bestCol)
    progress.done()
    print()
    print()
        
if __name__ == "__main__":
    board = []
    init_board(board)
    counter = 0
    #poslist = []
    while(hasSpace(board)!=0):
        if(isComplete(board)!=0):
            break
        Movebest(board,counter)
        counter = 1 - counter
        view.viewBackToFront(board)
        time.sleep(1)
       # print(isComplete(board))
    #view.viewBackToFront(board)
        
        
                        

        
    

    

    
    
