# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from .block import Block
from .writer import Writer
from .exception import *

class CWriter(Writer):
    _hdr = ''

    def __init__(self, blocks):
        super(CWriter,self).__init__(blocks)

    def __repr__(self):
        pass

    def save(self, filename):
        f = open(filename,"w")
        f.write(self._hdr)
        f.close()

    def build(self):
        for block in self.blocks:
            prefix = block.name + "_"
            base_name = "BASE_" + block.name
            self._hdr += "\n\n#ifndef _" + block.name + "_REG_\n"
            self._hdr += "#define _" + block.name + "_REG_\n"

            self._hdr += "#define " + base_name
            self._hdr += " ("+hex(block.base_address) + ")\n"
            # TODO: Add Descriptions for this block or not?
            for register in block.registers:
                # TODO: Build register
                reg_prefix = prefix + register.name
                reg_name = "REG_" + reg_prefix

                self._hdr += "#define "+reg_name 
                self._hdr += " "*(40 - len(reg_name))
                self._hdr += "(*(volatile unsigned int *) ("
                self._hdr += base_name + " + " + hex(register.offset) + "))\n"                
                
                for bit in register.bits:
                    if bit.name.lower() == "reserved":
                        continue
                    # TODO: Build bits information
                    bit_prefix = reg_prefix + "_" + bit.name.upper()
                    bit_name = "BIT_" + bit_prefix
                    self._hdr += "    #define " + bit_name
                    self._hdr += " "*(36 - len(bit_name))
                    self._hdr += "(" + self._get_bit_field(bit.high, bit.low) + ")\n"
                self._hdr +="\n"

            # TODO: print endif
            self._hdr += "#endif /* _" + block.name + "_REG_\n"

        # Do I Need to Make Test Code for testing REGISTER R/W based on Type?

    def _get_bit_field(self, high, low):
        """Return hex format bit field"""
        ret = 2**(high+1) - 2**low
        #print("%d, %d : %s"%(high, low, hex(ret)))
        return "0x%x"%ret
        
