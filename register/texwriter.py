# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from .block     import Block
from .exception import ProcedureError
from .writer    import Writer
from .register  import Register
from .bit       import Bit

from mako.template import Template

from markdown import Markdown

import string

class TexWriter(Writer):

    CH_PER_BIT = 4  # letter in a bit size

    def save(self, filename):
        f = open(filename,'w')
        f.write(self.output)
        f.close()

    def build(self):
        tpl = Template(filename='tpl/wrapper.tpl')
        reg = Register("FSM\_CMD", 4, 0x93, "Test Description")

        blocks = self.buildBitstable(self.blocks)

        blocks = self.sanitize(blocks)

        self.output = tpl.render_unicode(blocks=blocks)

    def buildBitstable(self, blocks):
        """ Build 16bits tables per register
        """
        myblks = []
        for blk in blocks:
            myblk = Block(blk.name, blk.base_address, blk.description)

            for reg in blk.registers:
                myreg = Register(reg.name, reg.offset, reg.por, reg.desc)
                myreg.row0 = []
                myreg.row1 = []
                myreg.bits = []
                for bit in reg.bits:
                    myreg.bits.append(Bit(bit.name, bit.range, bit.type, bit.description))
                    # Bit splitting codes
                    if bit.low >= 16:
                        # first row
                        myreg.row0.append(Bit(bit.name, bit.range, bit.type, bit.description))
                    elif bit.high <= 15:
                        # second row
                        myreg.row1.append(Bit(bit.name, bit.range, bit.type, bit.description))
                    else:
                        # first & second together
                        bit0 = Bit(bit.name, "%d:16"%bit.high, bit.type, bit.description)
                        bit1 = Bit(bit.name, "15:%d"%bit.low , bit.type, bit.description)
                        bit0.low = 16
                        bit1.high = 15
                        myreg.row0.append(bit0)
                        myreg.row1.append(bit1)

                myblk.registers.append(myreg)

            myblks.append(myblk)

        return myblks

    def removeRoot(self, t):
        msg =  t.replace("<root>","").replace("</root>","").replace('_','\_')
        return msg

    def sanitize(self, blocks):
        """ Sanitize strings to fit TeX
        """
        self.md = Markdown(None, extensions=['latex'])

        myblocks = []

        for blk in blocks:
            myblocks.append(self.sanitizeBlock(blk))

        return myblocks

    def sanitizeBlock(self, block):
        name = self.removeRoot(self.md.convert(block.name))
        description = self.removeRoot(self.md.convert(block.description))

        registers = []

        for reg in block.registers:
            registers.append(self.sanitizeRegister(reg))

        blk = Block(name, block.base_address, description)
        blk.registers = registers
        return blk

    def sanitizeRegister(self, register):
        name = self.removeRoot(self.md.convert(register.name))
        desc = self.removeRoot(self.md.convert(register.desc))

        bits = []
        row0 = []
        row1 = []

        for bit in register.bits:
            bits.append(self.sanitizeBit(bit))

        for bit in register.row0:
            row0.append(self.sanitizeBit(bit))

        for bit in register.row1:
            row1.append(self.sanitizeBit(bit))


        reg = Register(name, register.offset, register.por, desc)
        reg.bits = bits
        reg.row0 = row0
        reg.row1 = row1
        return reg

    def sanitizeBit(self, bit):
        name = self.removeRoot(self.md.convert(bit.name))
        description = self.removeRoot(self.md.convert(bit.description))

        return Bit(name, bit.range, bit.type, description)
