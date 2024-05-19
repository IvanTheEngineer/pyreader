## pip install pipenv
## pipenv install pypdf
## pipenv install easyocr
## pipenv install opencv-python
## pipenv install matplotlib
## pipenv install reportlab
## pipenv run python reading.py

## scanning searchable pdf from text

from pypdf import PdfReader

reader = PdfReader("sample.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)

## scanning image and plotting results

import easyocr

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('sample.png')
print(result)

import cv2
from matplotlib import pyplot as plt
img = cv2.imread("sample.png")

for detection in result:
    topleft = tuple([int(val) for val in detection[0][0]])
    bottomright = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_PLAIN
    img = cv2.rectangle(img, topleft, bottomright, (0,255,0), 5)
    img = cv2.putText(img, text, topleft, font, 1, (0, 0, 0), 2, cv2.LINE_AA )

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()

## generating pdf from image scan

img = cv2.imread("sampledoc.jpg")
height, width, channels = img.shape
result = reader.readtext('sampledoc.jpg', width_ths=1)
print(result)

import reportlab
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("test.pdf", pagesize=(width, height))
for detection in result:
    fromleft = detection[0][0][0]
    fromtop = detection[0][2][1]
    text = detection[1]
    canvas.drawString(fromleft, height - fromtop, text)
canvas.save()

for detection in result:
    topleft = tuple([int(val) for val in detection[0][0]])
    bottomright = tuple([int(val) for val in detection[0][2]])
    text = detection[1]
    font = cv2.FONT_HERSHEY_PLAIN
    img = cv2.rectangle(img, topleft, bottomright, (0,255,0), 5)
    img = cv2.putText(img, text, topleft, font, 1, (0, 0, 0), 2, cv2.LINE_AA )

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()