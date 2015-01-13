#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import getopt,sys

from register import parser,xlsxwriter

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:o:')
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    filename = args[0]
    outputName = args[0].split('.')[0]+'.xlsx'

    for o,a in opts:
        if o == '-f':
            continue
        elif o == '-o':
            outputName = a
        else:
            assert False, "unhandled option"

    blocks = parser.parser([filename])
    writer = xlsxwriter.XlsxWriter(blocks)

    writer.build()
    print("Writing into : %s"%outputName)
    writer.save(outputName)

if __name__ == "__main__":
    main()

