from __future__ import print_function
import fitz
import sys

bitness = "64 bit" if sys.maxsize > 2 ** 32 else "32 bit"

print("Python:", sys.version, bitness, "on", sys.platform, "\n")
print(fitz.__doc__)

m1 = fitz.Matrix(101)
m2 = fitz.Matrix(-101)
m3 = m1 * m2
print()
print("Checking matrix multiplication.")
print("Rotations of same positive and negative angle should result in identity.")
print("Result of abs(Identity - rot+ * rot-) =", abs(m3 - fitz.Identity))
