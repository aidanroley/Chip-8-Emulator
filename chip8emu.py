from pathlib import Path
import pygame
from display import Display
from memory import Memory
from CPU import CPU


class chip8emu:
   width = 64
   height = 32
   scale = 10

   def __init__(self):
      pygame.init()
      home = str(Path.home())
      data_folder = input("Enter path to .ch8 file from your user directory (press enter for default)\n")
      if (data_folder == ""):
         data_folder = str(Path("/Downloads/IBM Logo.ch8"))
      else:
         data_folder = str(Path("/" + data_folder))
      screen = Display.display_set(self.width, self.height, self.scale)
      self.memory = Memory()
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

if (__name__ == '__main__'):

   emulator = chip8emu()
   emulator.run()