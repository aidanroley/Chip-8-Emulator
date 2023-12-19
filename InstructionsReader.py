import pygame
from memory import Memory
from display import Display
from clock import Clock
from keymap import Keymap
import random


class InstructionsReader:  

   def convertHex(memoryArray):
    hex_strings = [hex(element) for element in memoryArray]
    hex_string = ' '.join(hex_strings)
    return hex_string
   
   def fetch(hexArray):
      decoded = (hexArray[Memory.pc]) + (hexArray[Memory.pc+1])
      #print(Memory.pc)
      firstnibble = decoded[0]
      secondnibble = decoded[1]
      thirdnibble = decoded[2]
      fourthnibble = decoded[3]
      secondbyte = decoded[2] + decoded[3]
      twelvebit = decoded[1] + decoded[2] + decoded[3]
      Memory.pc += 2
      return decoded, firstnibble, secondnibble, thirdnibble, fourthnibble, secondbyte, twelvebit
   
   def decodeAndExecute(hexArray, fetched, first, x, y, n, nn, nnn, chip8_screen, screen):
   
     def push(nnn):
       Memory.stack_pointer += 1
       Memory.stack[Memory.stack_pointer] = Memory.pc
       Memory.pc = int(nnn, 16)

     def pop():
        value = Memory.stack[Memory.stack_pointer]
        Memory.stack_pointer -= 1
        return value
     #print(fetched)
     def clearscreen():
        chip8_screen.fill((0,0,0))

     def jump(fetched, nnn):
        #print(Memory.pc)
        Memory.pc = int(nnn, 16)
     def Subroutine(nnn):
        push(nnn)

     def returnFromSub():
        Memory.pc = pop()

     def ifEqualSkip(x, nn):
        hehe = int(nn, 16)
        yay = Memory.vregister[int(x, 16)]
        if int(nn, 16) == Memory.vregister[int(x, 16)]:
           Memory.pc += 2

     def ifNotEqualSkip(x, nn):
        if int(nn, 16) != Memory.vregister[int(x, 16)]:
           Memory.pc += 2

     def fiveSkip(x, y):
        if Memory.vregister[int(x, 16)] == Memory.vregister[int(y, 16)]:
           Memory.pc += 2

     def nineSkip(x, y):
        if Memory.vregister[int(x, 16)] != Memory.vregister[int(y, 16)]:
           Memory.pc += 2

     def Set(x, nn):
        Memory.vregister[int(x, 16)] = int(nn, 16)

     def Add(x, nn):
        Memory.vregister[int(x, 16)] = (Memory.vregister[int(x, 16)] + int(nn, 16)) % 256

     def SetIndex(nnn):
        nnn_index = (int(nnn, 16))
        Memory.indexregister = nnn_index
        ##print(Memory.indexregister)

     def eightSet(x, y):
        Memory.vregister[int(x, 16)] =  Memory.vregister[int(y, 16)]

     def binaryOR(x, y):
        Memory.vregister[int(x, 16)] =  Memory.vregister[int(x, 16)] | Memory.vregister[int(y, 16)]

     def binaryAND(x, y):
        Memory.vregister[int(x, 16)] =  Memory.vregister[int(x, 16)] & Memory.vregister[int(y, 16)]

     def binaryXOR(x, y):
        Memory.vregister[int(x, 16)] =  Memory.vregister[int(x, 16)] ^ Memory.vregister[int(y, 16)]

     def eightAdd(x, y):
       sum_value = Memory.vregister[int(x, 16)] + Memory.vregister[int(y, 16)]
       if sum_value > 255:
        Memory.vregister[15] = 1
        sum_value = sum_value % 256  
       else:
        Memory.vregister[15] = 0
       Memory.vregister[int(x, 16)] = sum_value


     def fiveSubtract(x, y):
        if Memory.vregister[int(x, 16)] >= Memory.vregister[int(y, 16)]:
           Memory.vregister[15] = 1  
        else:
           Memory.vregister[15] = 0  

        Memory.vregister[int(x, 16)] = (Memory.vregister[int(x, 16)] - Memory.vregister[int(y, 16)]) % 256

       

     def sevenSubtract(x, y):
         if Memory.vregister[int(y, 16)] >= Memory.vregister[int(x, 16)]:
           Memory.vregister[15] = 1  
         else:
           Memory.vregister[15] = 0  

         Memory.vregister[int(x, 16)] = (Memory.vregister[int(y, 16)] - Memory.vregister[int(x, 16)]) % 256

     def sixShift(x, y): #Make vx equal to vy if i want as well
        value = Memory.vregister[int(x, 16)]
        Memory.vregister[int(x, 16)] = Memory.vregister[int(y, 16)]
        Memory.vregister[15] = value & 0x1
        Memory.vregister[int(x, 16)] = value >> 1

     def eShift(x, y):
        value = Memory.vregister[int(x, 16)]
        Memory.vregister[int(x, 16)] = Memory.vregister[int(y, 16)]
        Memory.vregister[15] = (value >> 7) & 0x1
        Memory.vregister[int(x, 16)] = (value << 1) & 0xFF

     def jumpWithOffset(nnn):
        Memory.pc = int(nnn, 16) + Memory.vregister[0]

     def Random(x, nn):
        random_number = random.randint(0,255)
        Memory.vregister[int(x, 16)] = random_number & int(nn, 16)

     def skipKeyIfPressed(x):
        key_value = Memory.vregister[int(x, 16)]
        hexit = hex(key_value)
        key_value_int = int(hexit, 16)
        mapped_key = Keymap.REVERSE_KEY_MAP.get(key_value_int)
        if mapped_key is not None:
           keys_pressed = pygame.key.get_pressed()
           if keys_pressed[mapped_key]:
            Memory.pc += 2

     def skipKeyIfNotPressed(x):
        key_value = Memory.vregister[int(x, 16)]
        hexit = hex(key_value)
        key_value_int = int(hexit, 16)
        mapped_key = Keymap.REVERSE_KEY_MAP.get(key_value_int)
        if mapped_key is not None:
           keys_pressed = pygame.key.get_pressed()
           if not keys_pressed[mapped_key]:
            Memory.pc += 2
     def getKey(x):
          Memory.pc -= 2
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                 chip8_key = Keymap.KEY_MAP.get(event.key)
                 if chip8_key is not None:   
                  Memory.vregister[int(x, 16)] = chip8_key
                  key_pressed = True
                  
                  

     def sevenTimer(x):
        Memory.vregister[int(x, 16)] = Clock.delay_timer

     def fiveTimer(x):
        Clock.delay_timer = Memory.vregister[int(x, 16)]

     def eightTimer(x):
        Clock.sound_timer = Memory.vregister[int(x, 16)]

     def addToIndex(x):
        x_value = Memory.vregister[int(x, 16)]
        total_value = Memory.indexregister + x_value
        if total_value > 0xFFF:
         Memory.vregister[15] = 1  # Set VF to 1 if overflow occurs
        Memory.indexregister = total_value & 0xFFF  # Ensure it remains a 12-bit value
      


     def fontCharacter(x):
       x_index = int(x, 16)
       character = Memory.vregister[x_index]
       font_size = 5
       if isinstance(character, str):
          Memory.indexregister = 80 + (int(character, 16) * font_size)
       elif isinstance(character, int):
          Memory.indexregister = 80 + (character * font_size)


     def decConversion(x, hexArray):
      val = Memory.vregister[int(x, 16)]
      hundreds = val // 100
      tens = (val // 10) % 10
      ones = val % 10
      hexArray[Memory.indexregister] = format(hundreds, '02x')
      hexArray[Memory.indexregister + 1] = format(tens, '02x')
      hexArray[Memory.indexregister + 2] = format(ones, '02x')

        
     
     def storeMemory(x, hexArray):
        x_index = int(x, 16)
        for index in range(x_index + 1):
          hexArray[Memory.indexregister + index] = format(Memory.vregister[index], '02x')

     def loadMemory(x, hexArray):
      x_ind = int(x, 16)
      temp_index = Memory.indexregister
      for index in range(x_ind + 1):
       if isinstance(hexArray[temp_index + index], str):
        Memory.vregister[index] = int(hexArray[temp_index + index], 16)
       else:
          Memory.vregister[index] = hexArray[temp_index + index]

    





     def Displaymethod(hexArray, x, y, n):
       x_coord = Memory.vregister[int(x, 16)] % 64
       y_coord = Memory.vregister[int(y, 16)] % 32
       nbruh = int(n, 16)
       Memory.vregister[15] = 0  # Reset the collision flag

       for row in range(nbruh):
        sprite_byte = int(hexArray[Memory.indexregister + row], 16)
        for col in range(8):  # Each byte has 8 bits, hence 8 columns
            sprite_pixel = sprite_byte & (0x80 >> col)
            if sprite_pixel != 0:
                screen_x = (x_coord + col) % 64
                screen_y = (y_coord + row) % 32

                # Check for collision and XOR the pixel
                if chip8_screen.get_at((screen_x, screen_y)) == (255, 255, 255, 255):
                    Memory.vregister[15] = 1  # Set collision flag
                    chip8_screen.set_at((screen_x, screen_y), (0, 0, 0))
                else:
                    chip8_screen.set_at((screen_x, screen_y), (255, 255, 255))
    
    # Update the display here or outside this function depending on your design
       # scaled_surface = pygame.transform.scale(chip8_screen, (64 * 10, 32 * 10))
        #screen.blit(scaled_surface, (0, 0))
        #pygame.display.flip()




                

     if first.isdigit() and n.isdigit():
        first_num = int(first)
        n_num = int(n)
        if ((first_num == 0) & (n_num == 0)):
         clearscreen()
         scaled_surface = pygame.transform.scale(chip8_screen, (64 * 10, 32 * 10))
         screen.blit(scaled_surface, (0, 0))
         pygame.display.flip()

     if first.isdigit():
        if first == '2':
           Subroutine(nnn)
     

     if first.isdigit() and n == 'e':
        if first == '0':
           returnFromSub()
          

     if first.isdigit():
        first_num = int(first)
        if (first) == '1':
         jump(fetched, nnn)
         

     if first.isdigit():
        first_num = int(first)
        if (first) == '6':
           Set(x, nn)
      
     if first.isdigit():
        first_num = int(first)
        if (first) == '7':
           Add(x ,nn) 

     if first.isdigit():
        first_num = int(first)
        if (first) == '3':
           ifEqualSkip(x,nn)

     if first.isdigit():
        first_num = int(first)
        if (first) == '4':
           ifNotEqualSkip(x,nn)

     if first.isdigit():
        if (first) == '5':
           fiveSkip(x, y)

     if first.isdigit():
        if (first) == '9':
           nineSkip(x, y)

     if first.isdigit():
        if (first) == '8':
           if n == '0':
              eightSet(x, y)
           elif n == '1':
              binaryOR(x, y)
           elif n == '2':
              binaryAND(x, y)
           elif n == '3':
              binaryXOR(x, y)
           elif n == '4':
              eightAdd(x, y)
           elif n == '5':
              fiveSubtract(x, y)
           elif n == '6':
              sixShift(x, y)
           elif n == '7':
              sevenSubtract(x, y)
           elif n == 'e':
              eShift(x, y)

     if first == 'a':
        SetIndex(nnn)

     if first == 'b':
        jumpWithOffset(nnn)

     if first == 'c':
        Random(x, nn)

     if first == 'd':
        Displaymethod(hexArray,x,y,n)
        scaled_surface = pygame.transform.scale(chip8_screen, (64 * 10, 32 * 10))
        screen.blit(scaled_surface, (0, 0))
        #pygame.display.update()

     if (first == 'e') & (n == 'e'):
        skipKeyIfPressed(x)

     if (first == 'e') & (y == 'a'):
        skipKeyIfNotPressed(x)

     if (first == 'f') & (n == '7'):
        sevenTimer(x)

     if (first == 'f') & (y == '1') & (n == '5'):
        fiveTimer(x)

     if (first == 'f') & (n == '8'):
        eightTimer(x)

     if (first == 'f') & (n == 'e'):
        addToIndex(x)

     if (first == 'f') & (n == 'a'):
        getKey(x)

     if (first == 'f') & (n == '9'):
        fontCharacter(x)

     if (first == 'f') & (n == '3'):
        decConversion(x, hexArray)

     if (first == 'f') & (y == '5') & (n == '5'):
        storeMemory(x, hexArray)

     if (first == 'f') & (y == '6') & (n == '5'):
        loadMemory(x, hexArray)



        
     #return hexArray
          
 
       
         
     
         
         
      
  
  

      
   
      
      
     
     
     
   

