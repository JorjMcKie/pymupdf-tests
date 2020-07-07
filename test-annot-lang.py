# -*- coding: utf-8 -*-
from __future__ import print_function, division
import os, sys

import fitz

print(fitz.__doc__)
if fitz.VersionBind.split(".") < ["1", "17", "0"]:
    sys.exit("Need PyMuPDF v1.17.0 or later.")

outfile = os.path.abspath(__file__).replace(".py", ".pdf")


def table_cells(rect=(0, 0, 1, 1), cols=1, rows=1):
    """Return a list of (rows x cols) equal sized rectangles.

    Notes:
        A little utility to fill a given area with table cells of equal size.
    Args:
        rect: rect_like to use as the table area
        rows: number of rows
        cols: number of columns
    Returns:
        A list with <rows> items, where each item is a list of <cols>
        PyMuPDF Rect objects of equal size, jointly covering 'rect'.
    """
    rect = fitz.Rect(rect)  # ensure that this is a Rect
    if rect.isEmpty or rect.isInfinite:
        raise ValueError("rect must be finite and not empty")
    tl = rect.tl

    # compute width and height of one table cell
    height = rect.height / rows
    width = rect.width / cols

    # first rectangle
    r = fitz.Rect(tl, tl.x + width, tl.y + height)

    delta_h = (width, 0, width, 0)  # diff to next right rect
    delta_v = (0, height, 0, height)  # diff to next lower rect

    row = [r]  # make the first row
    for i in range(1, cols):
        r += delta_h  # build next rect to the right
        row.append(r)

    rects = [row]  # make the result starting with the first row
    for i in range(1, rows):
        row = rects[i - 1]  # take previously appended row
        nrow = []  # the new row to append
        for r in row:  # for each previous cell, add its downward copy
            nrow.append(r + delta_v)
        rects.append(nrow)  # append new row to result

    return rects


doc = fitz.open()  # new PDF
page = doc.newPage()  # new page

text = r"""This is a text of mixed languages to generate FreeText annotations with automatic font selection - a feature new in MuPDF v1.17.
Euro: €, general Latin and other signs: | ~ ° ² ³ ñ ä ö ü ß â ¿ ¡ µ ¶ œ ¼ ½ ¾ ‰
Japan: 熊野三山本願所は、 15世紀末以降における熊野三山 （熊野本宮、 熊野新宮
Greece: Στα ερείπια της πόλης, που ήταν ένα σημαντικό
Korea: 에듀롬은 하나의 계정으로 전 세계 고등교육 기관의 인터넷에 접속할
Russia: Ко времени восшествия на престол Якова I в значительной
China: 北京作为城市的历史 可以追溯到 3,000 年前。西周初年， 周武王封召公奭于燕國。
Devanagari (not supported): नि:शुल्क ज्ञानको लागी लाई धन्यबाद""".splitlines()

blue = (0, 0, 1)
red = (1, 0, 0)
gold = (1, 1, 0)
green = (0, 1, 0)

# make the rectangles for filling in above text lines
tl = page.rect.tl + (72, 144)  # some distance from page rect corners
br = page.rect.br - (72, 144)
rect = fitz.Rect(tl, br)
cells = table_cells(rect, cols=1, rows=len(text))

for i in range(len(text)):
    annot = page.addFreetextAnnot(
        cells[i][0] + (2, 2, -2, -2),  # table cell, somewhat shrinked
        text[i],
        fontsize=16,
        fontname="he",  # used for non-CJK characters only!
        align=fitz.TEXT_ALIGN_CENTER,
        text_color=blue,
    )
    annot.setBorder(width=1.0)
    annot.update(fill_color=gold, border_color=green)

doc.save(outfile)
