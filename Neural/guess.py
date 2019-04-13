import network
import pickle
import imgConv
from matplotlib import pyplot as plt

network_file= open("network.pickle","rb")
net = pickle.load(network_file)

data = imgConv.imageprepare("image.png")
for i in range(784):
    data[i] = [data[i]]

newArr = [[0 for d in range(28)] for y in range(28)]
k = 0
for i in range(28):
    for j in range(28):
        newArr[i][j] = data[k][0]
        k = k+1

print("Guess: "+str(net.guess(data)))
plt.imshow(newArr, interpolation='nearest')
plt.show()

