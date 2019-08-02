from PIL import Image
import numpy
from math_recognition import preprocess, Symbol

symbols = []
pixels = []


def prepare_image(img_path):
    img = Image.open(img_path).convert('L')
    threshold = 150
    img_bw = img.point(lambda p: p > threshold and 255)
    img_arr_binary = numpy.array(img_bw)
    img_bin = preprocess.bw_to_binary(img_arr_binary)
    return img_bin, img


def segment_image(img_path):
    expression_img, img = prepare_image(img_path)
    rows = len(expression_img)
    cols = len(expression_img[0])
    for i in range(0,rows-1):
        for j in range(0, cols-1):
            if expression_img[i][j] == 1:
                pixels2 = check_pixels_around(expression_img, i, j)
                listX = [pixels2[0][0] for pixels2[0] in pixels2]
                listY = [pixels2[0][1] for pixels2[0] in pixels2]
                top = min(listX)
                bottom = max(listX)
                left = min(listY)
                right = max(listY)
                single_im = Symbol.Symbol(image = img.crop((left - 2, top - 2, right + 2, bottom + 2)), top=top, left=left, right=right, bottom=bottom)
                symbols.append(single_im)
                for el in pixels2:
                    expression_img[el[0]][el[1]] = 0
                pixels2 =[]; listX=[]; listY=[]; global pixels; pixels =[]
    return symbols


def check_pixels_around(img,x,y):
    rows = len(img)
    cols = len(img[0])
    pixels.append([x,y])

    if x != 0:
        if img[x-1][y] == 1 and [x-1,y] not in pixels:
            check_pixels_around(img,x-1,y)
    if x != 0 and y != 0:
        if img[x-1][y-1] == 1 and [x-1, y-1] not in pixels:
            check_pixels_around(img, x-1, y-1)
    if y != 0:
        if img[x][y-1] == 1 and [x, y-1] not in pixels:
            check_pixels_around(img, x, y-1)
    if x != rows-1 and y!=0:
        if img[x+1][y-1] == 1 and [x+1, y-1] not in pixels:
            check_pixels_around(img, x+1, y-1)
    if x != rows-1:
        if img[x+1][y] == 1 and [x+1, y] not in pixels:
            check_pixels_around(img, x+1, y)
    if x != rows-1 and y != cols-1:
        if img[x+1][y+1] == 1 and [x+1, y+1] not in pixels:
            check_pixels_around(img, x+1, y+1)
    if y != cols-1:
        if img[x][y+1] == 1 and [x, y+1] not in pixels:
            check_pixels_around(img, x, y+1)
    if x != 0 and y != cols - 1 and [x-1, y+1] not in pixels:
        if img[x-1][y+1] == 1:
            check_pixels_around(img, x-1, y+1)
    return pixels

