# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:16:49 2022

@author: user
"""

# pip install pillow  #一個python的影像處理庫，pytesseract依賴
# pip install pytesseract
# 安裝tesseract
# http://www.juzicode.com/image-tesseract-ocr5-install-on-windows/
# http://jasonyychiu.blogspot.com/2020/09/pythonpytesseract-pytesseractpytesserac.html
# pip install pyocr
# pip install wand
# 安裝ImageMagick
# https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows
# 安裝Ghostscript
# https://segmentfault.com/a/1190000041342989
from wand.image import Image
from  PIL import Image as PI
import pyocr
import pyocr.builders
import pytesseract
import io
# 需將Tesseract.exe路徑新增到程式碼中
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[2]


req_image = []
final_text = []

#image_pdf = Image(filename='C:/Users/user/Desktop/SDS_pdf/16-GHS_SDS_清罐劑(HP5406).pdf', resolution=300)
image_pdf = Image(filename='C:/Users/user/Desktop/SDS_pdf/18-GHS_SDS_次氯酸鈉(漂白水)1101101-R.pdf', resolution=300)
image_jpeg = image_pdf.convert('jpeg')

for img in image_jpeg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))


for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    final_text.append(txt)

