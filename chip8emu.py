import threading
from pathlib import Path
import pygame
from memory import Memory
from CPU import CPU
from clock import Clock

def displayset(chip8_width, chip8_height, scale):
    width, height = chip8_width * scale, chip8_height * scale
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
    pygame.display.set_caption('Chip8')
    return screen

class chip8emu:

    def __init__(self):
        home = str(Path.home())
        data_folder = input("Enter name of ch8 file with extension\n")
        if (data_folder == ""):
         data_folder = str(Path("/Downloads/Game_ROMS/pong2.rom"))
        else:
         data_folder = str(Path("/Downloads/Game_ROMS/" + data_folder))
        print(data_folder)
        print(home + "\\Downloads\\sound.wav")
        pygame.init()
        Clock.beep_sound = pygame.mixer.Sound(home + "\\Downloads\\Game_ROMS\\sound.wav")
       
        
        self.scale = 10  
        self.chip8_screen = pygame.Surface((64, 32))  # Chip8 native resolution
        self.screen = displayset(64, 32, self.scale)
        self.memory = Memory()  
        filename = home + data_folder
        self.memory.getfile(filename)
        self.memory.load_fontset()
        memory_array = self.memory.getmemory()
        self.cpu = CPU(memory_array, self.chip8_screen, self.screen)  # Pass the Chip8 screen surface to the CPU


   
#Instance of the emulator
emulator = chip8emu()

