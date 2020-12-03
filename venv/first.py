import pygame
import sys


def main():
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    fps = 60
    ex = False
    ra = 100
    rx = 0
    ry = 0
    rect_color = pygame.Color('green')
    pygame.draw.rect(screen, rect_color, (rx, ry, ra, ra))

    running = True
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if (x < rx or x > rx + ra or y < ry or y > ry + ra):

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    sys.exit(main())
print('')
