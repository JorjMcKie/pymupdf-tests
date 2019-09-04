#! python
from __future__ import print_function
import fitz
import sys

print("")
print(__file__)
print("".ljust(30, "-"))
print(fitz.__doc__)

datei = "001003ED.pdf"
doc = fitz.open(datei)

toc = doc.getToC(True)
print("Simple ToC of file", datei, "".ljust(50, "="))
for t in toc:
    print(t)

toc = doc.getToC(False)
print("\n\n\nExtended ToC of file", datei, "".ljust(50, "="))
for t in toc:
    print(t)
