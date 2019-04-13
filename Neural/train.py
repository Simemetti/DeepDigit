import mnist_loader
import os
import pickle

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
import network

net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)

network_file= open("network.pickle","wb")
pickle.dump(net,network_file)
network_file.close()

print("Network saved")
 
