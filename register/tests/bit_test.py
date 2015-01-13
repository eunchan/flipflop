#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import unittest

from ..bit import Bit
from ..exception import XmlFormatError

class TestBit(unittest.TestCase):
    def test_rangeCheck(self):
        with self.assertRaises(XmlFormatError):
            bit = Bit('index','6;4', 'rwc', 
                'This should raise XmlFormatError exception, because range '
                'is seperated by semicolon(";") not by colon(":").')

if __name__ == "__main__":
    unittest.main()
