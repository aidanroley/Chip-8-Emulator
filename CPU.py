import pygame  
from memory import Memory 
from InstructionsReader import InstructionsReader
from clock import Clock
import cProfile
import pstats
DELAY_TIMER_EVENT = pygame.USEREVENT + 1
class CPU:

    def __init__(self, memoryArray, chip8_screen, screen): ## i will use an array as a stack instead of importing a stack 
        pygame.time.set_timer(DELAY_TIMER_EVENT, int(1000 / 60))
       
        
        hexArray = InstructionsReader.convertHex(memoryArray)
        hexArray = hexArray.split()
        hexArray = [i[2:] for i in hexArray]
        for i in range (len(hexArray)):
            if len(hexArray[i]) == 1:
                hexArray[i] = '0' + hexArray[i]
        
        while Memory.pc < len(hexArray):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     pygame.quit()
                elif event.type == DELAY_TIMER_EVENT:
                    if Clock.delay_timer > 0:
                        Clock.delay_timer -= 1
                     


            fetched, first, x, y, n, nn, nnn = InstructionsReader.fetch(hexArray)
            beep_sound = pygame.mixer.Sound("C:\\Users\\bridg\\Downloads\\bruh.wav")
            current_time = pygame.time.get_ticks()
            if current_time - Clock.last_timer_update >= 1000 / 60:
                #if Clock.delay_timer > 0:
                    #Clock.delay_timer -= 1
                if Clock.sound_timer > 0:
                    Clock.sound_timer -= 1
            
            Clock.last_timer_update = current_time

            if Clock.sound_timer > 0:
                if not pygame.mixer.get_busy():  # Check if a sound is already playing
                    beep_sound.play()  # Play the beep sound
                else:
                    beep_sound.stop()
            #print(Memory.pc)
            print(fetched)
                    
            self.profile = cProfile.Profile()
            self.profile.enable()
            InstructionsReader.decodeAndExecute(hexArray, fetched, first, x, y, n, nn, nnn, chip8_screen, screen)
            self.profile.disable()
            stats = pstats.Stats(self.profile).sort_stats('cumtime')
           # stats.print_stats()

            Clock.main_clock.tick(60)
            #fps = Clock.main_clock.get_fps()
            #print(f"Current FPS: {fps}")
            
            pygame.display.flip()
  



