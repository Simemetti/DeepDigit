import mnist_loader
import pickle
import network2

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network2.Network([784, 30, 10], cost=network2.CrossEntropyCost)
net.large_weight_initializer()
net.SGD(training_data, 30, 10, 0.5, evaluation_data=test_data, lmbda=5.0, monitor_evaluation_accuracy=True,
        monitor_training_accuracy=True)

network_file = open("network.pickle", "wb")
pickle.dump(net, network_file)
network_file.close()

print("Network saved")
