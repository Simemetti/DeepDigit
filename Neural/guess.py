from PIL import Image

import sys
import imgConv
from digit_splitter import split_digits
from networks_manager import guess

if len(sys.argv) == 1:
    path = "image.jpg"
else:
    path = sys.argv[1]
im = Image.open(path).convert('L')

images = split_digits(im)
data = []

for single_image in images:
    if single_image != " ":
        data.append(imgConv.imageprepare(single_image))
    else:
        data.append(" ")
answer = ""

for single_data in data:
    if single_data != " ":
        for i in range(784):
            single_data[i] = [single_data[i]]
        answer = answer + str(guess(single_data))
    else:
        answer = answer + " "

print('\U0001F914' + " my guess is " + answer)
