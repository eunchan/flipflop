#!/usr/bin/python

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from textwrap import wrap, fill, dedent

class Register:
    """Register element in a Block.

    Register class contains a register information for a block. each register
    has unique name and offset inside a block.

    """

    name = ''
    offset = 0
    por = 0
    desc = ''
    bits = []
    row0 = []
    row1 = []
    por_bits = []

    def __init__(self, name, offset, por, desc):
        """Constructor of Register class.

        Args:
            name (str): The Register name. 'A-Z and _' are only allowed.
            offset (int): Register's offset address based on 'base_address' of
                Block. 'offset' should be described as hexadecimal format in
                XML.
            por (int): Register's Power On Reset value. This value should be
                also specified as hex format.
            desc (str): Description of Register. desc contains brief explanation
                of this register, which might be usages, examples.

        """
        self.name = name
        self.offset = offset
        self.por = por
        self.desc = desc
        self.por_bits = []
        for i in reversed(range(32)):
            if por & (0x1 << i) :
                self.por_bits.append(1)
            else:
                self.por_bits.append(0)
