import board

DIMENSIONS = board.DIMENSIONS
board_game = [[-1 for _ in range(DIMENSIONS)] for _ in range(DIMENSIONS)]
moves_made = 0;
move_list = []
legal_moves = [[2,1], [1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
start_square_x = None;
start_square_y = None;



def print_board():
    max_width = len(str(max(map(max, board_game)))) + 1

    for row in board_game:
        for element in row:
            print(f"{element:{max_width}}", end="")
        print()

#checks if a move is allowed
def is_valid(x,y, move):
    global board
    new_x = x + move[1]  
    new_y = y + move[0]  
    
    if new_x < 0 or new_y < 0 or new_x > DIMENSIONS-1 or new_y > DIMENSIONS-1:
        return False
    if board_game[new_x][new_y] != -1:
        return False
    return True

#recursive function used to find the path for the knight
def find_path(x,y):
    global moves_made
    global board_game
    moves_reamaning = legal_moves
    if(moves_made >=(DIMENSIONS*DIMENSIONS)-1):
        if(moves_made == (DIMENSIONS*DIMENSIONS)-1):
            print_board()
        return True

    move = choose_move(x,y,moves_reamaning)
    if move is None:
        return False
    x += move[1]
    y += move[0]
    moves_made += 1
    moves_reamaning = [item for item in moves_reamaning if item != move]
    board_game[x][y] = moves_made
    move_list.append([x,y])
    if (find_path(x,y)):
        return True
    restore(x,y)

#restores the previous data after doing a wrong move that lead to no solution -- backtracking
def restore(x,y):
    global board_game
    global moves_made
    board_game[x][y] = -1
    move_list.pop()
    update = move_list[-1]
    x = update[0]
    y = update[1]
    moves_reamaning.append(move)
    moves_made-=1


#this fucntion helps choose the best move, using Warnsdorff's rule we prioritize the square that leaves the knight with the fewest legal moves.
def choose_move(x,y,moves_reamaning):
    best_move = None
    allowed_moves = 100
    for move in moves_reamaning:
        if(is_valid(x,y,move)):
            temp = legal_moves_left(x,y,move)
            if temp < allowed_moves:
                allowed_moves = temp
                best_move = move
    return best_move

def legal_moves_left(x,y,move):
    new_x = x + move[1]
    new_y = y + move[0]
    total = 0
    for move in legal_moves:
        if(is_valid(new_x,new_y,move)):
            total+= 1

    return total

def algorithm():
    user_input_column = int(input("\nPlease enter the starting column for the knight: ")) 
    user_input_row = int(input("Please enter the starting row for the knight: "))
    

    if user_input_column < 0 or user_input_column > DIMENSIONS or user_input_row <0 or user_input_row > DIMENSIONS:
        print("Enter a valid coordinate.")
        return False
    start_square = [user_input_row, user_input_column]
    start_square_x = user_input_row
    start_square_y = user_input_column
    board_game[start_square_x][start_square_y] = 0
    move_list.append(start_square)
    find_path(start_square_x,start_square_y)
    if(move_list[-1] == start_square or DIMENSIONS < 5):
        print("There exists no knights tour from this square")
        return False
    return True