import pygame

class Display:

    def display_set(width, height, scale):
        pygame.init()
        screen = pygame.display.set_mode((width * scale, height * scale))
        print("ok")
        pygame.display.set_caption('Chip-8')
        screen.fill((0, 0, 0))
        pygame.display.flip()
        return screen
