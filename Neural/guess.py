import pickle
import imgConv
import image_slicer

network_file = open("network.pickle", "rb")
net = pickle.load(network_file)

image_slicer.slice('image.jpg', 2)
image_slicer.slice('image_01_01.png',2)
image_slicer.slice('image_01_02.png',2)

data = []
data.append(imgConv.imageprepare("image_01_01_01_01.png"))
data.append(imgConv.imageprepare("image_01_01_01_02.png"))
data.append(imgConv.imageprepare("image_01_02_01_01.png"))
data.append(imgConv.imageprepare("image_01_02_01_02.png"))


for single_data in data:
    for i in range(784):
        single_data[i] = [single_data[i]]
    print("Guess: " + str(net.guess(single_data)))
