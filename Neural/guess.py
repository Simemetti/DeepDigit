import imgConv
from PIL import Image
from digit_splitter import split_digits
from networks_manager import guess

im = Image.open('image.jpg').convert('L')

images = split_digits(im,4)
data = []

for single_image in images:
    data.append(imgConv.imageprepare(single_image))
answer = ""

for single_data in data:
    for i in range(784):
        single_data[i] = [single_data[i]]
    answer = answer + str(guess(single_data))

print('\U0001F914'+ " my guess is " + answer)