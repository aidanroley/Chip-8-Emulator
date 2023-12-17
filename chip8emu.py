from pathlib import Path
import pygame
from display import Display
from memory import Memory
from CPU import CPU

width = 64
height = 32
scale = 10
class chip8emu:

   def __init__(self):
    pygame.init()
    screen = Display.displayset(width, height, scale)
    self.memory = Memory()
    home = str(Path.home())
    data_folder = str(Path("/Downloads/IBM Logo.ch8"))
    filename = home + data_folder
    self.memory.getfile(filename)
    self.memory.load_fontset()
    memory_array = self.memory.getmemory()
    self.cpu = CPU(memory_array, screen)

   def run(self):
      isRunning = True
      while isRunning:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               isRunning = False

    ###  
       

      

emulator = chip8emu()
emulator.run()