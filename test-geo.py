from __future__ import print_function
import fitz
import sys

print("Python:", sys.version, "on", sys.platform, "\n")
print(fitz.__doc__)
m1 = fitz.Matrix(101)
m2 = fitz.Matrix(-101)
m3 = m1 * m2
print()
print("Checking matrix multiplication.")
print("Rotations of same positive and negative angle should result in identity.")
print("Result of abs(Identity - rot+ * rot-) =", abs(m3 - fitz.Identity))
