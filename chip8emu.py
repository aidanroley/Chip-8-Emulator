import pygame
from display import Display
from memory import Memory

class chip8emu:
   def __init__(self):
    pygame.init()
    display = Display(64, 32, 10)
    self.memory = Memory()
    filename = "C:\\Users\\bridg\\Downloads\\15 Puzzle [Roger Ivie].ch8"
    self.memory.getfile(filename)

   def run(self):
    isRunning = True
    while isRunning:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
          isRunning = False

    ###  
       

      

emulator = chip8emu()
emulator.run()