import pygame
from copy import deepcopy


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 20
        self.color = 'green'

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    pygame.draw.rect(surface, self.color,
                                     (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(surface, 'white',
                                 (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        pos = [mouse_pos[0] - self.left, mouse_pos[1] - self.top]
        if 0 <= pos[0] <= self.cell_size * self.width and \
                0 <= pos[1] <= self.cell_size * self.height:
            pos[0] = pos[0] // self.cell_size
            pos[1] = pos[1] // self.cell_size
            return pos[0], pos[1]
        return None

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


class Life(Board):
    def on_click(self, cell_coords):
        new_value = abs(self.board[cell_coords[1]][cell_coords[0]] - 1)
        self.board[cell_coords[1]][cell_coords[0]] = new_value

    def next_move(self):
        prev_state = deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                neighbours = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i != 0 or j != 0:
                            neighbours += prev_state[(y + i) % self.height][(x + j) % self.width]
                if neighbours == 3:
                    self.board[y][x] = 1
                elif neighbours != 2:
                    self.board[y][x] = 0


pygame.init()
screen = pygame.display.set_mode((630, 430))
board = Life(30, 20)
running = True
edit_mode = True
clock = pygame.time.Clock()
fps = 60
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT and edit_mode:
                board.get_click(event.pos)
            elif event.button == pygame.BUTTON_RIGHT:
                edit_mode = not edit_mode
            elif event.button == pygame.BUTTON_WHEELDOWN:
                fps = max(fps - 5, 1)
            elif event.button == pygame.BUTTON_WHEELUP:
                fps += 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                edit_mode = not edit_mode
    if not edit_mode:
        board.next_move()
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
    clock.tick(fps)
