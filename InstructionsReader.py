import pygame
from memory import Memory
class InstructionsReader:

   def convertHex(memoryArray):
    hex_strings = [hex(element) for element in memoryArray]
    hex_string = ' '.join(hex_strings)
    return hex_string
   
   def fetch(hexArray):
      global pc
      decoded = (hexArray[Memory.pc]) + (hexArray[Memory.pc+1])
      print(Memory.pc)
      firstnibble = decoded[0]
      secondnibble = decoded[1]
      thirdnibble = decoded[2]
      fourthnibble = decoded[3]
      secondbyte = decoded[2] + decoded[3]
      twelvebit = decoded[1] + decoded[2] + decoded[3]
      Memory.pc += 2
      return decoded, firstnibble, secondnibble, thirdnibble, fourthnibble, secondbyte, twelvebit
   
   def decodeAndExecute(fetched, first, x, y, n, nn, nnn, screen):
     global pc
     ##print(fetched)
   def clearscreen(screen):
      global pc
      screen.fill((255,0,0))
      pygame.display.flip()

   def jump(fetched, nnn):
      global pc
      Memory.pc = int(nnn, 16)

   def Set(x, nn):
      Memory.vregister[int(x, 16)] = int(nn, 16)
    
      if first.isdigit() and n.isdigit():
        first_num = int(first)
        n_num = int(n)
        if (first_num & n_num) == 0:
         clearscreen(screen)

      if first.isdigit():
        first_num = int(first)
        if (first_num) == 1:
         jump(fetched, nnn)

      if first.isdigit():
        first_num = int(first)
        if (first_num) == 6:
           Set(x, nn)
          
       
         
     
         
         
      
  
  ## def jump():
      
  
 ##  def setregistervx():
      

   ##def addvaluevx():
      

  ## def setindexregisterI():
      

   ##def displaydraw():
      


      
   
      
      
     
     
     
   

