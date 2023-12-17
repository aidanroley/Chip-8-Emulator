import pygame  
from memory import Memory 
from InstructionsReader import InstructionsReader
class CPU:

    def __init__(self, memoryArray, screen): ## i will use an array as a stack instead of importing a stack 
        self.stack = [0] * 16
        self.stack_pointer = -1
        self.index_register = 0
        self.delay_timer = 0
        self.sound_timer = 0
        hexArray = InstructionsReader.convertHex(memoryArray)
        hexArray = hexArray.split()
        hexArray = [i[2:] for i in hexArray]
        for i in range (len(hexArray)):
            if len(hexArray[i]) == 1:
                hexArray[i] = '0' + hexArray[i]
        
        while Memory.pc < len(hexArray) - 3300:
            fetched, first, x, y, n, nn, nnn = InstructionsReader.fetch(hexArray)
            print(Memory.pc)
            ##print(fetched)
            InstructionsReader.decodeAndExecute(fetched, first, x, y, n, nn, nnn, screen)
            ##print(pc)
           ## print("pointer")

            ##print(pc)
        ##print(hexArray)
        ##print(len(hexArray))

    def decrement_timers(self):
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1


    def push(self, value):
        self.stack_pointer += 1
        self.stack[self.stack_pointer] = value

    def pop(self):
        value = self.stack[self.stack_pointer]
        self.stack_pointer -+ 1
        return value


