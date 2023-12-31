
import pygame as p
import board
import time
import algorithm
import sys

new_recursion_limit = 2500  # Set the new recursion limit here
sys.setrecursionlimit(new_recursion_limit)
DIMENSIONS = board.DIMENSIONS
min_window_size = 550
max_window_size = 650
for window_size in range(min_window_size, max_window_size + 1):
    if window_size % DIMENSIONS == 0:
        break
SQ_SIZE = window_size//DIMENSIONS
MAX_FPS = 60
IMAGE = {}
IMAGE["wN"] = p.transform.scale(p.image.load("images/wN.png") , (SQ_SIZE,SQ_SIZE))
move_sfx = None
end_sfx = None
end = False
current = 0
speed = None

def main():
    global move_sfx
    global end_sfx
    global speed
    p.init()
    p.mixer.init()
    new_window_title = "Knight's tour"
    p.display.set_caption(new_window_title)
    move_sfx = p.mixer.Sound("sounds/move-self.mp3")
    end_sfx = p.mixer.Sound("sounds/Checkmate.mp3")
    if algorithm.algorithm():
        running = True
        speed = float(input("Enter a number between 0 and 1 to change the animation speed: "))
        if speed < 0:
            print("Please enter a positive number. ")
            running = False
        screen = p.display.set_mode((window_size, window_size))
        clock = p.time.Clock()
        screen.fill(p.Color("white"))
        gs = board.game_state()
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False

            draw_game_state(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()

        p.quit()  # Quit Pygame when done


def draw_game_state(screen, gs):
    draw_board(screen, gs.board)
    draw_pieces(screen, gs.board)


def draw_board(screen, board):

    colors = [p.Color(233, 237, 204), p.Color(119, 153, 84)]
    colors_highlight = [p.Color(235,125,105), p.Color(212,109,81)]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            if board[r][c] == "--":
                color = colors[((r+c) %2)]
            if board[r][c] == "-+":
                color = colors_highlight[((r+c) %2)]
            p.draw.rect(screen, color, p.Rect(r*SQ_SIZE,c*SQ_SIZE,SQ_SIZE,SQ_SIZE))

def draw_pieces(screen, board):
    global current
    global move_sfx
    global end_sfx
    global end
    global speed
    
    current_move = algorithm.move_list[current]
    board[current_move[1]][current_move[0]] = "wN"
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            knight = board[r][c]
            if knight == "wN":
                screen.blit(IMAGE["wN"], p.Rect(r*SQ_SIZE,c*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    board[current_move[1]][current_move[0]] = "-+"
    time.sleep(speed)
    if current < len(algorithm.move_list) -1:
        current+=1
        if(current >= 2):
            move_sfx.play()
    if(current_move  == algorithm.move_list[-1] and end == False):
        end_sfx.play()
        end = True
            



if __name__ == "__main__":
    main()


