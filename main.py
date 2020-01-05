import pygame
import minimax as mm
from init import init_board
from checkComplete import isComplete,hasSpace

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
LGREEN      =    (125,200,20)
RED      = ( 255,   0,   0)
BLUE     = (   10,   100, 255)

def drawO(i,j,k,color=WHITE):
    pygame.draw.ellipse(screen, color, [285+(50/4)*j+50*k, 52.5+(150*(3-i))+25*j, 45, 22.5], 4) 
def drawX(i,j,k,color=BLUE):
    pygame.draw.line(screen,color,[285+(50/4)*j+50*k,55+(150*(3-i))+25*j],[325+(50/4)*j+50*k,70+(150*(3-i))+25*j],4)
    pygame.draw.line(screen,color,[290+(50/4)*j+50*k,70+(150*(3-i))+25*j],[320+(50/4)*j+50*k,55+(150*(3-i))+25*j],4)
def drawSelected(i,j,k,board):
    pygame.draw.line(screen,RED,[275+(50*k)+(50/4)*j,50+(25*j)+(150*(3-i))],[275+(50/4)*(j+1)+(50*k),75+(25*j)+(150*(3-i))],2)
    pygame.draw.line(screen,RED,[325+(50*k)+(50/4)*j,50+(25*j)+(150*(3-i))],[325+(50/4)*(j+1)+(50*k),75+(25*j)+(150*(3-i))],2)
    pygame.draw.line(screen,RED,[275+(50/4)*(j) + 50*k,50+(150*(3-i)+(25*j))],[325+(50/4)*(j)+50*k,50+(150*(3-i))+(25*j)],2)
    pygame.draw.line(screen,RED,[275+(50/4)*(j+1) + 50*k,50+(150*(3-i)+(25*(j+1)))],[325+(50/4)*(j+1)+50*k,50+(150*(3-i))+(25*(j+1))],2)
    if(board[i][j][k]==3):
        drawX(i,j,k,RED)
    elif(board[i][j][k]==5):
        drawO(i,j,k,RED)
# Loop until the user clicks the close button.
done = False
pygame.init()

size = (700, 650)
screen = pygame.display.set_mode(size)
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
board = []
init_board(board)
counter = 0
level = -1
col = -1
row = -1
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]
            level = int((event.pos[1] - 50)/150)
            #print(level)
            row = ((y-50-(level*150))/25)

            row = int(row)
            if(row>=4 or row<0):
                row = -1
            #print(row)
            col = (x - 275 - row*50/4)/50

            col = int(col)
            if(col>=4 or col<0):
                col = -1
            #print(col)
            level = 3-level
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if(col!= -1 and row!=-1):
                    if(board[level][row][col]==1 and counter == 0 and isComplete(board)==0):
                        board[level][row][col] = 3
                        counter = 1
            elif event.button == 3:
                if(isComplete(board)!= 0 or hasSpace(board)==0):
                    counter = 0
                    board = []
                    init_board(board)

            
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    if(hasSpace(board)==0):
        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('Draw , Right Click to restart', True, GREEN, BLUE) 
        textRect = text.get_rect() 
        textRect.center = (350, 25) 
        screen.blit(text, textRect) 
    if(isComplete(board)!=0):
        winner = isComplete(board)
        font = pygame.font.Font('freesansbold.ttf', 32) 
        if(winner == 3):
            wc = 'X'
        else:
            wc = 'O'
        text = font.render(wc+' has won the game! Right Click to restart', True, GREEN, BLUE) 
        textRect = text.get_rect() 
        textRect.center = (350, 25) 
        screen.blit(text, textRect) 

    for i in range(4):
        pygame.draw.line(screen, GREEN, [275, 50+(150*i)], [475, 50+(150*i)], 2)
        pygame.draw.line(screen,GREEN,[325,150+(150*i)],[525,150+(150*i)],2)
        pygame.draw.line(screen,GREEN,[275,50+(150*i)],[325,150+(150*i)],2)
        pygame.draw.line(screen,GREEN,[475,50+(150*i)],[525,150+(150*i)],2)
        for j in range(3):
            pygame.draw.line(screen,GREEN,[325+(50*j),50+(150*i)],[375+(50*j),150+(150*i)],1)
            pygame.draw.line(screen,GREEN,[275+(50/4)*(j+1),50+(150*i)+(100/4)*(j+1)],[475+(50/4)*(j+1),50+(150*i)+(100/4)*(j+1)],1)
    pygame.draw.line(screen,GREEN,[275,50],[275,500],1)
    pygame.draw.line(screen,GREEN,[525,150],[525,600],1)
    '''for i in range(3): #for drawing partial lines
        pygame.draw.line(screen,GREEN,[325,150+150*i],[325,200 + 150*i],1)
        pygame.draw.line(screen,GREEN,[475,150+150*i],[475,200+150*i],1)'''
    pygame.draw.line(screen,GREEN,[325,150],[325,600],1)
    pygame.draw.line(screen,GREEN,[475,50],[475,500],1)
    if(isComplete(board)==0 and counter == 1):
        mm.Movebest(board,counter)
        counter = 1 - counter
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if(board[i][j][k]==3):
                    drawX(i,j,k)
                elif(board[i][j][k]==5):
                    drawO(i,j,k)
    if(row!= -1 and col!= -1):
        drawSelected(level,row,col,board)

    '''for i in range(4): #for drawing all Os and all Xs
        for j in range(4):
            for k in range(4):
                pygame.draw.ellipse(screen, WHITE, [285+(50/4)*j+50*k, 52.5+(150*(3-i))+25*j, 45, 22.5], 2) 
                pygame.draw.line(screen,BLUE,[285+(50/4)*j+50*k,55+(150*(3-i))+25*j],[325+(50/4)*j+50*k,70+(150*(3-i))+25*j],4)
                pygame.draw.line(screen,BLUE,[290+(50/4)*j+50*k,70+(150*(3-i))+25*j],[320+(50/4)*j+50*k,55+(150*(3-i))+25*j],4)
    '''
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()