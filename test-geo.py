from __future__ import print_function
import fitz
import sys
import time

bitness = "64 bit" if sys.maxsize > 2 ** 32 else "32 bit"

print("Python:", sys.version, bitness, "on", sys.platform, "\n")
print(fitz.__doc__)

alpha = 255
m1 = fitz.Matrix(alpha)
m2 = fitz.Matrix(-alpha)
m3 = m1 * m2
print()
print("Checking 'Matrix(%i) * Matrix(-%i) == Identity'." % (alpha, alpha))
print("Deviation: %g" % abs(m3 - fitz.Identity))

repeats = 10000
t0 = time.perf_counter()
for i in range(repeats):
    m3 = m1 * m2
t1 = time.perf_counter()
quot = (t1 - t0) / repeats
print("Average multiplication time: %g sec" % quot)
