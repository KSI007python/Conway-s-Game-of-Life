import pygame
import time
import copy

screen = pygame.display.set_mode((700, 800))

running = True

Grid = [[0 for i in range(70)] for i in range(70)]

play = False

# Grid[1][1] = 0

def ProcessGrid(x, y):
    global Grid
    newGrid = copy.deepcopy(Grid)
    for i in range(70):
        if i != 0:
            pygame.draw.line(screen, (255, 255, 255), (x+10, y+i*10), (x+690, y+i*10))
            pygame.draw.line(screen, (255, 255, 255), (x+i*10, y+10), (x+i*10, y+690))
    for i in range(1, len(Grid)-1):
        for j in range(1, len(Grid)-1):
            if Grid[i][j]:
                pygame.draw.rect(screen, (255, 255, 255), (i*10, j*10, 10, 10))

            if play:
                alive_cells = 0
                cellsToCheck = [
                    [i+1, j],
                    [i-1, j],
                    [i, j+1],
                    [i, j-1],
                    [i+1, j+1],
                    [i+1, j-1],
                    [i-1, j+1],
                    [i-1, j-1],
                ]
                for cell in cellsToCheck:
                    if Grid[cell[0]][cell[1]] == 1:
                        alive_cells += 1

                if alive_cells == 3 and Grid[i][j] == 0:
                    newGrid[i][j] = 1
                elif (alive_cells < 2 or alive_cells > 3) and Grid[i][j] == 1 :
                    newGrid[i][j] = 0
                else:
                    newGrid[i][j] = Grid[i][j]

            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX//10 == i and mouseY//10 == j and mouse_click:
                newGrid[i][j] = 1
                if keys[pygame.K_e]:
                    newGrid[i][j] = 0
    Grid = newGrid

X, Y = 0, 0

mouse_click = False

def playButton():
    global play
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (255, 255, 255), (290, 725, 70, 50), 2)
    if mouseX > 290 and mouseX < 360 and mouseY > 725 and mouseY < 775:
        pygame.draw.rect(screen, (100, 100, 100), (292, 727, 67, 47))
        if mouse_click:
            if play:
                play = False
            else:
                play = True
            time.sleep(0.1)
    if not play:
        pygame.draw.polygon(screen, (255, 255, 255), ((310, 735), (345, 750), (310, 765)), 2)
    else:
        pygame.draw.rect(screen, (255, 255, 255), (310, 735, 10, 30), 2)
        pygame.draw.rect(screen, (255, 255, 255), (330, 735, 10, 30), 2)

while running:

    screen.fill((0, 0, 0))

    ProcessGrid(X, Y)

    playButton()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_c]:
        Grid = [[0 for i in range(70)] for i in range(70)]

    if keys[pygame.K_p]:
        if not play:
            play = True
        else:
            play = False
        time.sleep(0.2)

    if play:
        time.sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = False

    pygame.display.update()