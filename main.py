import pygame, sys, random

maze_size = 20
maze = [[0,*[4 for _ in range (maze_size - 1)]], *[[1 for _ in range (maze_size)] for _ in range (maze_size - 1)]]
root = [0, 0]

def print_maze():
    for i in maze:
        for j in i:
            print(j, end=' ')
        print()

def draw_maze():
    for i in range (maze_size):
        for j in range (maze_size):
            if maze[i][j] == 1:
                pygame.draw.line(screen, tunnel_color, (j*50+37, i*50+37+12), (j*50+37, (i-1)*50+37-12), 25)
            elif maze[i][j] == 2:
                pygame.draw.line(screen, tunnel_color, (j*50+37-12, i*50+37), ((j+1)*50+37+12, i*50+37), 25)
            elif maze[i][j] == 3:
                pygame.draw.line(screen, tunnel_color, (j*50+37, i*50+37-12), (j*50+37, (i+1)*50+37+12), 25)
            elif maze[i][j] == 4:
                pygame.draw.line(screen, tunnel_color, (j*50+37+12, i*50+37), ((j-1)*50+37-12, i*50+37), 25)


def update_maze():
    directions = [1, 2, 3, 4]
    if root[0] == 0:
        directions.remove(4)
    elif root[0] == maze_size - 1:
        directions.remove(2)
    if root[1] == 0:
        directions.remove(1)
    elif root[1] == maze_size - 1:
        directions.remove(3)
    maze[root[1]][root[0]] = random.choice(directions)
    if maze[root[1]][root[0]] ==1:
        root[1] -= 1
    elif maze[root[1]][root[0]] ==2:
        root[0] += 1
    elif maze[root[1]][root[0]] ==3:
        root[1] += 1
    elif maze[root[1]][root[0]] ==4:
        root[0] -= 1
    maze[root[1]][root[0]] = 0

pygame.init()

screen = pygame.display.set_mode((1028,1028))
pygame.display.set_caption('Origin Shift Maze Generation Algorithm Implementation in Python by Indibar Sarkar')
screen_color = '#000080'
tunnel_color = 'black'

print_maze()
print()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(screen_color)
    # pygame.draw.line(screen,'red', (50, 50), (100, 50), 10)
    # pygame.draw.line(screen,'blue', (100, 50), (100, 100), 10)
    # pygame.draw.line(screen,'yellow', (100, 100), (50, 100), 10)
    # pygame.draw.line(screen,'green', (50, 100), (50, 50), 10)
    draw_maze()
    pygame.display.update()
    update_maze()
    print_maze()
    print()