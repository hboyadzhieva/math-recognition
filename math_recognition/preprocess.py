import numpy as np
import math


def im_grayscale_to_bw(img):
    threshold = 240
    img_binary = img.point(lambda p: p > threshold and 255)
    img_arr_binary = np.array(img_binary)
    return img_arr_binary


def bw_to_binary(img):
    rows = len(img)
    cols = len(img[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if img[i][j] == 255:
                img[i][j] = 0
            elif img[i][j] == 0:
                img[i][j] = 1
    return img


def im_grayscale_to_binary(img):
    img = im_grayscale_to_bw(img)
    return bw_to_binary(img)

def binary_to_bw(img):
    rows = len(img)
    cols = len(img)
    for i in range(0, rows):
        for j in range(0, cols):
            if img[i, j] == 0:
                img[i, j] = 255
            elif img[i][j] == 1:
                img[i, j] = 0
    return img


# resizes the image to a 45Xsomething, where the longer side takes 45 and the shorter gets proportional to not distort the original image
def resize(pil_image):
    size = 45,45
    width, height = pil_image.size
    pil_image.thumbnail(size)


def fill_edges(bin_image):
    size = 45
    x = len(bin_image)
    y = len(bin_image[0])
    new_img = np.zeros((45,45))
    if x < y:
        left_side = int(math.floor((size - x)/2))
        right_side = size - x - left_side
        k = 0
        for i in range(left_side, size - right_side):
            for j in range(0, size-1):
                new_img[i,j] = bin_image[k][j]
            k+=1
        new_img = new_img.astype(np.uint8)


    if y < x:
        bottom = int(math.floor((size - y)/2))
        top = size - y - bottom
        k = 0
        for i in range(0, size-1):
            for j in range(bottom, size - top):
                new_img[i,j] = bin_image[i][k]
                k+=1
            k=0
        new_img = new_img.astype(np.uint8)

    return new_img

