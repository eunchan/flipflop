# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from .exception import ProcedureError

class Writer(object):
    def __init__(self, blocks):
        self.blocks = blocks

    def save(self, filename):
        pass

    def build(self):
        pass

    def assign(self, blocks):
        if self.blocks:
            raise ProcedureError("blocks are assigned twice.")
        else:
            self.blocks = blocks
