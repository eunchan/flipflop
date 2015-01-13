#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import unittest

from ..xlsxwriter import XlsxWriter
from ..parser import parser
from ..exception import *

class TestXlsWriter(unittest.TestCase):
    def test_normal(self):
        blocks = parser(['register/examples/dma.xml'])
        writer = XlsxWriter(blocks)
        writer.build()

        writer.save('dma.xlsx')
        
        #self.assertIsNone('')

    def test_assignError(self):
        blocks = parser(['register/examples/dma.xml'])
        writer = XlsxWriter(blocks)

        with self.assertRaises(ProcedureError):
            writer.assign(blocks)

if __name__ == "__main__":
    unittest.main()
