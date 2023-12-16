import pygame
import time
import threading
from display import Display
from memory import Memory
from CPU import CPU

class chip8emu:

   home = str(Path.home())
   def __init__(self):
    pygame.init()
    display = Display(64, 32, 10)
    self.memory = Memory()
    filename = Home + "\\Downloads\\IBM Logo.ch8"
    self.memory.getfile(filename)
    self.memory.load_fontset()
    memory_array = self.memory.getmemory()
    self.cpu = CPU(memory_array)

   def run(self):
    isRunning = True
    while isRunning:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
          isRunning = False

    ###  
       

      

emulator = chip8emu()
emulator.run()