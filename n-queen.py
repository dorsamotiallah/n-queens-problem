import random 

board = []
queens = []

def initiate_board(n):
    count = n
    while (count>0):
        f = random.randint(0,n-1)
        s = random.randint(0,n-1)
        if(board[f][s] == 0 ):
            board[f][s] = 1 #ones are queens
            queens.append((f,s)) #position of queen in board 
            count -= 1

def attack_in_column(pos):
    count = 0 
    for q in queens:
        if(q != pos):
            if(q[1] == pos[1]):
                count += 1
    return count

def attack_in_row(pos):
    count = 0 
    for q in queens:
        if(q != pos):
            if(q[0] == pos[0]):
                count += 1
    return count

def attack_in_Diagonal(pos):
    count = 0 
    for q in queens:
        if(q != pos):
            if(abs(q[0]-pos[0]) == abs(q[1]-pos[1])):
                count += 1
    return count

def number_of_conflicts(pos):
    return attack_in_column(pos) + attack_in_row(pos) + attack_in_Diagonal(pos)

def find_best_destination(pos,col_conf,row_conf,Diag_conf): #pos is position of queen and col_conf,row_conf,Diag_conf are it's column,row,Diagonal conflicts count.
    m = min(col_conf,row_conf,Diag_conf)
    #m = col_conf
    minconflictpos = (-1,-1) # this position is not valid so is good for initilizing
    minconflictcount = n  #for each node real conflict can be n-1 so n will always be greater than real count of conflicts.
    thisconflictcount = -1
    if(m == col_conf):
        for i in range(len(board)):
            if(((i,pos[1]) not in queens) and i != pos[0]):
                movequeen((i,pos[1]),pos)
                thisconflictcount = number_of_conflicts((i,pos[1]))
                if(thisconflictcount < minconflictcount):
                    minconflictcount = thisconflictcount
                    minconflictpos = (i,pos[1])
                movequeen(pos,(i,pos[1]))
         
    elif(m == row_conf):
        row = board[pos[0]]
        for i in range(len(row)):
            if( i != pos[1] and ((pos[0],i) not in queens)):
                movequeen((pos[0],i),pos)
                thisconflictcount = number_of_conflicts((pos[0],i))
                if(thisconflictcount < minconflictcount):
                    minconflictcount = thisconflictcount
                    minconflictpos = (pos[0],i)
                movequeen(pos,(pos[0],i))
             
    elif(m == Diag_conf):
        j = n-1 
        for i in range(n):
            if((i != pos[1] and j!=pos[0]) and ((j,i) not in queens)):
                movequeen((j,i),pos)
                thisconflictcount = number_of_conflicts((j,i))
                if(thisconflictcount < minconflictcount):
                    minconflictcount = thisconflictcount
                    minconflictpos = (j,i)
                movequeen(pos,(j,i))
            j -= 1
    
                
    return (minconflictpos ,minconflictcount)

def draw_board():
    for row in board:
        print(row)
        
        
def movequeen(destination, origin):#moves second position to first.
    queens.remove(origin)
    queens.append(destination)
    board[destination[0]][destination[1]] = 1
    board[origin[0]][origin[1]] = 0

def board_has_conflict():
    for q in queens:
        if(number_of_conflicts(q)!= 0):
            return True
    return False
    
if __name__ == "__main__":
    inp = input("what is the size of game ?\nplease insert n: ")
    n = int(inp)
    board = [[ 0 for i in range(n) ] for j in range(n)] 
    initiate_board(n)
    draw_board()
    print('*'* (3*n))
    queensunderattack = queens[:]
    while( board_has_conflict()):
        minconflictpos = (-1,-1)
        minconflictcount = -1
        queenpos = random.choice(queensunderattack)#chooses a queen which has conflict
        col_conf = attack_in_column(queenpos)
        row_conf = attack_in_row(queenpos)
        diag_conf = attack_in_Diagonal(queenpos)
        minconflictpos , minconflictcount = find_best_destination(queenpos,col_conf,row_conf,diag_conf)
        movequeen(minconflictpos , queenpos)#move queen to minconflict position from all available positions.
        queensunderattack.remove(queenpos)
        if (minconflictcount > 0):
            queensunderattack.append(minconflictpos)
        draw_board()
        print('*'* (3*n))
    print('-'* (3*n))
    draw_board()