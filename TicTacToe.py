def show():
 line1 =" 1 | 2 | 3 "          #Framework of the TicTacToe game
 line2 ="___|___|__ "
 line3 =" 4 | 5 | 6 "
 line4 ="___|___|__ "
 line5 =" 7 | 8 | 9 "
 line6 ="   |   |   "

 global board                #Declare board global to access it
 boardlen=len(board)
 
 while(boardlen>0):         # Replace the element by symbol belonging to the player
   if(board[boardlen]!='Empty'): 
     
     if(str(boardlen)=='1' or str(boardlen)=='2' or str(boardlen)=='3'):
        line1=line1.replace(str(boardlen),board[boardlen])
     elif(str(boardlen)=='4' or str(boardlen)=='5' or str(boardlen)=='6'):
         
         line3=line3.replace(str(boardlen),board[boardlen])
         
     else:
         line5=line5.replace(str(boardlen),board[boardlen])
   boardlen-=1       
 print(line1)              #Print the current Situation of the game
 print(line2)
 print(line3)
 print(line4)
 print(line5)
 print(line6)


def rules(): 
    global board
    x=len(board)
    y=1
    #Testing for rows
    while(y<=9):
        if(board[y]==board[y+1] and board[y+1]==board[y+2] and board[y]!='Empty'):
            
            return 1
        else:
            y+=3
    y=1
    # Testing for Columns 
    while(y<=3):
        if(board[y]==board[y+3] and board[y+3]==board[y+6] and board[y]!='Empty'):
            
            return 1
        else:
            y+=1
    

    # testing for Diagonals
    if(board[1]==board[5] and board[5]==board[9] and board[1]!='Empty'):            
            return 1
    elif(board[3]==board[5] and board[5]==board[7] and board[3]!='Empty'):
            return 1
            
        
    return 0



 

moves=9                     # Declare Game essentials
playing=0                   # Max num of moves, Condition for draw and check if
draw=0                      # playing or winner has been found
player=1
board ={}

x=9
while(x>0):                # Declare an Empty Dictionery
    board[x]='Empty'
    x-=1



print("Let the game begin")
print("First to go gets X")

show()

while(moves>0 and playing==0):    #Check if 9 moves have been played and winner hasnt been found
    move=int(input("Enter Number of the place you want to use between 1 and 9 "))
    if(move<=9 and move>0):
        if(board[move]!='Empty'):
          print("This place is occupied")   #check if the user doesnt use an occupied location
        elif(player==1):
            board[move]='X'
            
            show()
            playing=rules()
            if(playing==1):
                print("Player 1 is the winner")
            player=0
            moves-=1
            if(moves>0 and playing==0):
                print("Player 2 plays now")
        else :
            board[move]='O'
            show()
            playing=rules()
            if(playing==1):
                print("Player 2 is the winner")
            player=1
            moves-=1
            if(moves>0 and playing==0):
                print("Player 1 plays now")
                         
if(moves==0 and playing==0):
    print("Game Over, Winner cannot be found it is a Draw")
