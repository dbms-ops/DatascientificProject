#!/usr/bin/env python3
# -*- coding: latin-1 -*-

# sourcery skip: remove-redundant-fstring, simplify-fstring-formatting, use-fstring-for-concatenation
import sys

myStr1 = "aÄBeC"
myStr2 = "A\u00c4B\U00000000e8C"

myStr3 = "A" + chr(0xC4) + "B" + chr(0xE8) + "C"


print("Default encoding:", sys.getdefaultencoding())

for aStr in myStr1, myStr2, myStr3:
    print(f"{0} strlen={1}".format(aStr, len(aStr)), end=" ")

bytes1 = aStr.encode()
bytes2 = aStr.encode("latin-1")

print(f"byteslen1 = {0}, byteslen2 = {1}".format(len(bytes1), len(bytes2)), end=" ")
