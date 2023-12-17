import pygame
class InstructionsReader:

   def convertHex(memoryArray):
    hex_strings = [hex(element) for element in memoryArray]
    hex_string = ' '.join(hex_strings)
    return hex_string
   
   def fetch(hexArray, pc):
        decoded = (hexArray[pc]) + (hexArray[pc+1])
        firstnibble = decoded[0]
        secondnibble = decoded[1]
        thirdnibble = decoded[2]
        fourthnibble = decoded[3]
        secondbyte = decoded[2] + decoded[3]
        twelvebit = decoded[1] + decoded[2] + decoded[3]
        pc += 2
        return decoded, pc, firstnibble, secondnibble, thirdnibble, fourthnibble, secondbyte, twelvebit
   
   def decodeandexecute(fetched, pc, first, x, y, n, nn, nnn, screen):
     def clearscreen(screen):
        screen.fill((255,0,0))
     if first.isdigit() and n.isdigit():
        first_num = int(first)
        n_num = int(n)
        if (first_num & n_num) == 0:
            clearscreen(screen)
         
     
         
         
      
  
  ## def jump():
      
  
 ##  def setregistervx():
      

   ##def addvaluevx():
      

  ## def setindexregisterI():
      

   ##def displaydraw():
      


      
   
      
      
     
     
     
   

