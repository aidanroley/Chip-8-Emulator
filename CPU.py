import pygame   

class CPU:

    def __init__(self): ## i will use an array as a stack instead of importing a stack 
        self.stack = [0] * 16
        self.stack_pointer = -1

    def push(self, value):
        self.stack_pointer += 1
        self.stack[self.stack_pointer] = value

    def pop(self):
        value = self.stack[self.stack_pointer]
        self.stack_pointer -+ 1
        return value


