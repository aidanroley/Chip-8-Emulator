import pygame

class Display:

    def __init__(self, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale
        self.screen = pygame.display.set_mode((width * scale, height * scale))
        pygame.display.set_caption('Chip8')
        self.screen.fill((0,0,0))
    