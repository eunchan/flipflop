# -*- coding: utf-8 -*-

class Block:

    # member variables
    name = ''
    base_address = 0x0
    description = ''
    registers = []

    def __init__(self):
        pass

    def __init__(self, name, base_address, desc):
        self.name = name
        self.base_address = base_address
        self.description = desc
