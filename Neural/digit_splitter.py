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


def split_digits(im, max_digits=None, dist_to_split=80):
    digits = []
    pix = im.load()
    column1 = 0
    column2 = 0
    valid = True
    i = 0

    while valid:
        while check_column(pix, column1, im.size[1]) == False and column1 < im.size[0] - 2:
            column1 += 1
        if (column2 != 0 and column1 - column2 >= dist_to_split):
            digits.append(" ")
        column2 = column1
        while check_column(pix, column2, im.size[1]) != False and column1 < im.size[0] - 2:
            column2 += 1
        if (column1 >= im.size[0] - 2 or column2 >= im.size[0] - 2 or i == max_digits):
            valid = False
        else:
            digits.append(split_horizontal(im.crop((column1, 0, column2, im.size[1]))))
            column1 = column2 + 1
            i += 1

    return digits


def split_horizontal(im):
    pix = im.load()
    row1 = 0

    while not check_row(pix, row1, im.size[0]):
        row1 += 1
    row2 = row1
    while check_row(pix, row2, im.size[0]) is not False:
        row2 += 1

    return im.crop((0, row1, im.size[0], row2))
