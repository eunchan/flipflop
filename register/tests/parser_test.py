#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import xml.etree.ElementTree as et

import unittest

#from parser import parser
from ..parser import parser

class TestParser(unittest.TestCase):
    def test_parser(self):
        self.assertIsNotNone(parser(['register/examples/dma.xml']))

if __name__ == "__main__":
    unittest.main()
