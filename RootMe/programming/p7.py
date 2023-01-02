import requests, re, base64
from PIL import Image, ImageDraw
from io import BytesIO
from random import randint
import zxing

temp_image_file = f'temp{randint(1e6, 9e6)}.png'
cookie = {'PHPSESSID':'SessionId'}

def main():
    download_image()
    draw_image(temp_image_file)
    decode_image(temp_image_file)

def download_image():
    r = requests.post('http://challenge01.root-me.org/programmation/ch7/', cookies=cookie)
    p = re.search(r'base64,\S+', r.text).group()[7:-1]
    im = Image.open(BytesIO(base64.b64decode(p)))
    im.save(temp_image_file)

def draw_image(img):
    im = Image.open(img)
    draw = ImageDraw.Draw(im)
    black = (0, 0, 0)
    white = (255, 255, 255)

    pixelSize = 9
    startX = 18
    startY = 18

    outer = pixelSize*7
    middle = pixelSize*6
    inner = pixelSize*5
    offset = 300 - pixelSize**2 - 1
    for (x, y) in [(startX, startY), (startX, offset), (offset, startY)]:
        draw.rectangle((x, y, x+outer, y+outer), black, black)
        draw.rectangle((x+pixelSize, y+pixelSize, x+middle, y+middle), white, white)
        draw.rectangle((x+pixelSize*2, y+pixelSize*2, x+inner, y+inner), black, black)
    im.save(img)

def decode_image(img):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(img)
    bar = barcode.raw[11:11+13]
    print('Barcode: %s\n' % bar)
    r = requests.post('http://challenge01.root-me.org/programmation/ch7/', data={'metu':bar}, cookies=cookie)
    print(r.text)

if __name__ == '__main__':
    main()