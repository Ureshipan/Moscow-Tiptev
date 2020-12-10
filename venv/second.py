import pygame
from copy import deepcopy

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width  # количество столбцов
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                coords = (self.left + x * self.cell_size,
                          self.top + y * self.cell_size,
                          self.cell_size,
                          self.cell_size)
                if self.board[y][x] == 1:
                    pygame.draw.rect(screen,
                                     pygame.Color('green'),
                                     coords, 0)

                pygame.draw.rect(screen,
                                 pygame.Color(100, 100, 100),
                                 coords, 1)

                # настройка внешнего вида

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def click(self, mouse_pos):
        col, row = self.is_cell(mouse_pos)
        if col:
            self.board[row][col] = 1


    def is_cell(self, mouse_pos):
        x, y = mouse_pos[0], mouse_pos[1]
        if (x < self.left or
                x > self.left + self.width * self.cell_size or
                y < self.top or
                y > self.top + self.height * self.cell_size):
            return None, None

        col = (x - self.left) // self.cell_size
        row = (y - self.top) // self.cell_size
        return col, row


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)

    def cell_in_board(i, j):
        return i > -1 and i < self.width and j > -1 and j < self.height
    def next_step(self):
        def cell_in_board(i, j):
            return i > -1 and i < self.width and j > -1 and j < self.height
        new_board = deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                s = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if cell_in_board(y + dy, x + dx):
                            s += self.board[y + dy][x + dx]
                s -= self.board[y][x]
                if s == 3:
                    new_board[y][x] = 1
                elif self.board[y][x] and (s < 2 or s > 3):
                    new_board[y][x] = 0
        self.board = deepcopy(new_board)



def main():
    pygame.init()
    size = w, h = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    pygame.display.set_caption('My play init')

    n_col = 30
    n_row = 30
    board = Life(n_col, n_row)
    cell_size = min(w, h) // (max(n_col, n_row) + 2)
    top = (h - cell_size * n_row) // 2
    left = (w - cell_size * n_col) // 2
    board.set_view(left, top, cell_size)

    ticks = 0
    speed = 10
    game = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    board.click(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                game = not game
                speed = 5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game = not game
                speed = 5
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  4:
                speed += 2
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  5:
                speed -= 2
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(speed)
        if game:
            board.next_step()
    pygame.quit()


if __name__ == '__main__':
    main()