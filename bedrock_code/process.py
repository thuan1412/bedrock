import cv2
import pytesseract
import numpy as np
import os
from pdf2image import convert_from_path
import tessact_

# def pdf_to_image(path):
#     pages = convert_from_path(path, 500)
#     for i in range(len(pages)):
#         pages[i].save('./uploads/' + str(i)+'.jpg', 'JPEG')
#     return len(pages)

class Form1(object):
    def __init__(self, fname):
        self.fname = fname
    def overwrite2image(self):
        # for i in range(self.n_pages):
        a = tessact_.get_field(self.fname)
        return a
            

# path = './0.jpg'
# f = Form1(path)
# print([i[0] for i in f.overwrite2image()])