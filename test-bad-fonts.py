import fitz

doc = fitz.open("has-bad-fonts.pdf")
print("File '%s' uses the following fonts on page 0:" % doc.name)
for f in doc.getPageFontList(0):
    print(f)
