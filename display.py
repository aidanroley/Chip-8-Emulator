import pygame

class Display:

    def displayset(width, height, scale):
        screen = pygame.display.set_mode((width * scale, height * scale))
        pygame.display.set_caption('Chip8')
        screen.fill((255,0,0))
        return screen
    