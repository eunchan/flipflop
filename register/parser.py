# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import xml.etree.ElementTree as et

import sys

# Internal modules
from .block import Block
from .register import Register
from .bit import Bit

def parser(filelists):
    
    blocks = []

    for filename in filelists:
        # TODO: Check file is exist or not
        
        # get root for a block
        root = et.parse(filename).getroot()
    
        # TODO: parse Block
        block = parseBlock(root)


        # TODO: parse bits inside a regsiter

        # append the block to blocks
        blocks.append(block)

    # TODO: return ip that contains blocks
    return blocks

def parseBlock(node):
    """Get block's informations.
    
    Each XML has one block element. It contains block's basic informations and
    registers.

    """
    name = node.find('name').text.strip()
    base_address = int(node.find('base_address').text.strip(),16)
    desc = trim(node.find('description').text)

    block = Block(name, base_address, desc)
    # parse Register inside a block
    block.registers = map(parseRegister, node.findall('register'))
    
    return block

def parseRegister(node):
    """Get node's information.

    Each Block has multiple register elements. These elements contains name,
    offset, reset value, description, and internal bits information.

    """
    name = node.find('name').text.strip()
    offset = int(node.find('offset').text,16)
    por = int(node.find('por').text,16)
    desc = trim(node.find('description').text)

    # Parse Bits inside a register
    register = Register(name, offset, por, desc)
    register.bits = map(parseBit, node.findall('bit'))
    
    return register

def parseBit(node):
    """Get bit structure."""
    name = node.find('name').text.strip()
    range = node.find('range').text.strip()
    type = node.find('type').text.strip()
    desc = trim(node.find('description').text)

    return Bit(name, range, type, desc)

def trim(desc):
    """Trim multiline texts.

    This code is copied from http://www.python.org/dev/peps/pep-0257 

    """
    if not desc:
        return ''

    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = desc.expandtabs().splitlines()

    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint

    for line in lines[1:]:
        stripped = line.lstrip()

        if stripped:
            indent = min(indent, len(line) - len(stripped))

    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]

    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())

    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)

    # return a single string:
    return '\n'.join(trimmed)
