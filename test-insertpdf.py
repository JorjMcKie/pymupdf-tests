from __future__ import print_function
import fitz
import sys
import os

print(fitz.__doc__)

flist = ("1.pdf", "2.pdf", "3.pdf", "4.pdf")
scriptdir = os.path.dirname(os.path.abspath(__file__))
print("scriptdir", scriptdir)
ofn = os.path.join(scriptdir, "output.pdf")
osize = 0
doc = fitz.open()
for f in flist:
    fname = os.path.join(scriptdir, f)
    x = fitz.open(fname)
    doc.insertPDF(x, links=1)
    fsize = os.path.getsize(fname)
    print(
        "inserted '%s' with %s %s and %s bytes"
        % (f, len(x), "pages" if len(x) > 1 else "page", fsize)
    )
    osize += fsize
    x.close()
    x = None

doc.save(ofn, deflate=True, garbage=4)
nsize = os.path.getsize(ofn)
dsize = nsize - osize
print("saved '%s' with %s pages" % (ofn, len(doc)))
print("sizes of all input %s, output %s, difference %s" % (osize, nsize, dsize))
