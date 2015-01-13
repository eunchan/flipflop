# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import unittest

from ..cwriter import CWriter
from ..parser import parser
from ..exception import *

class TestCWriter(unittest.TestCase):
    def test_normal(self):
        blocks = parser(['register/examples/dma.xml'])
        writer = CWriter(blocks)
        writer.build()

        writer.save('dma.h')
        
        #self.assertIsNone('')

if __name__ == "__main__":
    unittest.main()
