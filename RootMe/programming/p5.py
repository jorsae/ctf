"""
Password:
dtePZJgVAfaU
"""

import time
import re
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import base64
from io import BytesIO
import requests
import os

run = True
tries = 0
temp_image_file = 'tempasmfnpaosjf13tj13.png'

cookie = {'PHPSESSID':'sessionId'}
while run:
    r = requests.post('http://challenge01.root-me.org/programmation/ch8/', cookies=cookie)
    html = r.text
    p = re.search('base64,\S+', html).group()
    img = p[7:len(p) - 1]
    im = Image.open(BytesIO(base64.b64decode(img)))
    im = im.convert("RGBA")
    newimdata = []
    datas = im.getdata()

    for item in datas:
        if item[0] < 112 or item[1] < 112 or item[2] < 112:
            newimdata.append(item)
        else:
            newimdata.append((255, 255, 255))
    im.putdata(newimdata)

    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save(temp_image_file)
    text = pytesseract.image_to_string(Image.open(temp_image_file),config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6', lang='eng')
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    text = text.replace(',', '')
    text = text.replace('\'', '')
    r = requests.post('http://challenge01.root-me.org/programmation/ch8/', data={'cametu':text}, cookies=cookie, headers={'Accept-Language':'en-US;en;q=0.5'})
    if 'Failed, Try again.' in r.text:
        print('Failed: %s | %d' % (text, tries))
        tries += 1
        run = True
    else:
        print('Success! Text: %s | Tries: %d' % (text, tries))
        run = False
        print(r.text)
        os.remove(temp_image_file)