def check_column(pixels, column, h):
    for i in range(h - 1):
        if pixels[column, i] < 175:
            return i
    return False


def check_row(pixels, row, w):
    for i in range(w - 1):
        if pixels[i, row] < 175:
            return i
    return False


def split_digits(im, n=None):
    digits = []
    pix = im.load()
    column1 = 0
    valid = True
    i = 0
    while valid:
        while check_column(pix, column1, im.size[1]) == False and column1 < im.size[0] - 2:
            column1 += 1
        column2 = column1
        while check_column(pix, column2, im.size[1]) != False and column1 < im.size[0] - 2:
            column2 += 1
        if (column1 >= im.size[0] - 2 or column2 >= im.size[0] - 2 or i == n):
            valid = False
        else:
            digits.append(im.crop((column1, 0, column2, im.size[1])))
            column1 = column2 + 1
            i += 1

    return digits
