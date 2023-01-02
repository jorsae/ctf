"""
Used to get square width/height on qr code
black square = 10pixels
1 "square" on qr code = 10x10 pixels

Note: This was later changed to 9pixels
"""
import pyautogui as pag

black = (255, 255, 255)
def count_square():
    x, y = pag.position()
    count = 0
    for i in range(20):
        pag.moveTo(x + i, y)
        color = pag.pixel(x+i, y)
        if color == black:
            count+=1
    print(count)


def count_gap():
    x, y = pag.position()
    count = 0
    for i in range(1):
        pag.moveTo(x, y+i)
        color = pag.pixel(x, y+i)
        print(color)
        if color == black:
            count+=1
    print(count)

count_gap()
#count_square()