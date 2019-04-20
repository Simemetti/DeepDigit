import pickle

def guess(data):
    answers = {}

    for i in range(5):
        network_file = open("Networks/network"+str(i)+".pickle", "rb")
        net = pickle.load(network_file)
        guess = net.guess(data)
        print(guess)
        found = False
        for key in answers:
            if key == guess:
                found = True
        if found:
            answers[guess] += 1
        else:
            answers[guess] = 1
    return max(answers, key=answers.get)


