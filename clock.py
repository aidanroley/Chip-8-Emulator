import pygame

class Clock:
    delay_timer = 0
    sound_timer = 2
    main_clock = pygame.time.Clock()
    last_timer_update = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    beep_sound = 1