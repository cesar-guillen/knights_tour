DIMENSIONS = int(input("Choose board dimensions: "))
#initlializing the board that we will use to keep track of the knight in pygame

class game_state():
    def __init__(self):
        
        self.board = [["--" for _ in range(DIMENSIONS)] for _ in range(DIMENSIONS)]
        
        