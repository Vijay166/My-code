import pygame, sys
import numpy as np

pygame.init()

Width = 600
Height = Width
Line_width = 15
Board_Rows = 3
Board_Cols = 3
Square_size = Width//Board_Cols
Circle_radius = Square_size//3
Circle_width = 15
Cross_width = 25
Space = Square_size//4

#Colouring
Red_colour = (250, 0, 0)
Bg_colour = (20, 150, 150)
Line_colour = (153, 185, 185)
Circle_colour = (239, 231, 200)
Cross_colour = (66, 66, 66)

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('TIC-TAC-TOE')
screen.fill(Bg_colour)

#Board
board = np.zeros((Board_Rows, Board_Cols))

def draw_lines():
    #1st Horizontal line
    pygame.draw.line(screen, Line_colour, (0,Square_size), (Width, Square_size), Line_width)
    #2nd Horizontal line
    pygame.draw.line(screen, Line_colour, (0, 2*Square_size), (Width, 2*Square_size), Line_width)
    #1st Vertical line
    pygame.draw.line(screen, Line_colour, (Square_size, 0), (Square_size, Height), Line_width)
    #2nd Vertical line
    pygame.draw.line(screen, Line_colour, (2*Square_size, 0), (2*Square_size, Height), Line_width)

def draw_figure():
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            if board[row][col] == 1:
                pygame.draw.line(screen, Cross_colour, (col * Square_size + Space, row * Square_size + Square_size - Space), (col * Square_size + Square_size - Space, row * Square_size + Space), Cross_width)
                pygame.draw.line(screen, Cross_colour, (col * Square_size + Space, row * Square_size + Space), (col * Square_size + Square_size - Space, row * Square_size + Square_size - Space), Cross_width)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, Circle_colour, (int(col * Square_size + Square_size//2), int(row * Square_size + Square_size//2)), Circle_radius, Circle_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def whether_board_full():
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            if board[row][col] == 0:
                return False

    return True

def check_win(player):
    #Vertical win check
    for col in range(Board_Cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True
    #Horizontal win check
    for row in range(Board_Rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horozontal_win_line(row, player)
            return True
    #Ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_ascending_diagonal(player)
        return True
    #Decending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_decending_diagonal(player)
        return True
    return False

def draw_vertical_win_line(col, player):
    posX = col * Square_size + Square_size//2

    if player == 1:
        colour = Cross_colour
    elif player == 2:
        colour = Circle_colour

    pygame.draw.line(screen, colour, (posX, 15), (posX, Height - 15), 15)

def draw_horozontal_win_line(row, player):
    posY = row * Square_size + Square_size//2

    if player == 1:
        colour = Cross_colour
    elif player == 2:
        colour = Circle_colour

    pygame.draw.line(screen, colour, (15, posY), (Width - 15, posY), 15)

def draw_ascending_diagonal(player):
    if player == 1:
        colour = Cross_colour
    elif player == 2:
        colour = Circle_colour

    pygame.draw.line(screen, colour, (15,Height - 15), (Width - 15, 15), 15)

def draw_decending_diagonal(player):
    if player == 1:
        colour = Cross_colour
    elif player == 2:
        colour = Circle_colour

    pygame.draw.line(screen, colour, (15, 15), (Width - 15, Height - 15), 15)

def restart():
    screen.fill(Bg_colour)
    draw_lines()
    player = 1
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicking_row = int(mouseY // Square_size)
            clicking_col = int(mouseX // Square_size)

            if available_square(clicking_row, clicking_col):
                mark_square(clicking_row, clicking_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                draw_figure()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
