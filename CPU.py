import pygame   

class CPU:

    def __init__(self, memoryArray): ## i will use an array as a stack instead of importing a stack 
        self.stack = [0] * 16
        self.stack_pointer = -1
        self.pc = 0x200
        self.index_register = 0
        self.delay_timer = 0
        self.sound_timer = 0
        print(memoryArray)


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


