# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import re

from .exception import XmlFormatError

class Bit:
    """Bit data structure that is used in Register class.

    Bit data structure is used to defining fields inside register. For example,
    if a register contains 'busy' at 0 bit position, 'index[4:0]' inside 5 to 1
    bit position, Two Bit structure should be defined, which are busy and index.
    
    """
    #member variables
    name = ''
    range = ''
    high = 0
    low = 0
    type = '-'
    description = '-'

    def __init__(self):
        pass

    def __init__(self, name, range, type, description):
        self.name = name
        # check range conforms register format
        reg = re.compile('^[0-9:]+$')
        if not reg.match(range):
            raise XmlFormatError("range format is not correct: %s" % range)
        self.range = range
        self.high, self.low = self.rangeToHighLow(range)
        self.type = type
        self.description = description

    def rangeToHighLow(self, range):
        """Convert range string to two index value.

        Args:
            range (str): bit range index. This follows verilog array index
                format. For example, one bit structure spread bit position from
                5 to 1, range is '5:1'. The indexes shall be decimal format.
                hex, octa or binary format is not permitted.

        Returns:
            A pair of bit index values that the first value is always greater
            than or equal to second value. For example:

            (5,1) if range is '5:1'

        Raises:
            XmlFormatError: If range string does not follow 'x:y' or 'z', this
                exception occurs.

        """
        token = range.strip().split(':')

        if len(token) == 2:
            # Range
            return map(int,token)
        elif len(token) == 1:
            return (int(token[0]),int(token[0]))
            # Index
        else:
            # Error
            raise XmlFormatError("range format is not correct: %s" % range)
