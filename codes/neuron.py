import random

class neuron:

    weights = []

    def __init__(self, n_weights):
        self.weights = [random.uniform(-5, 5) for x in range(n_weights)]

    def sum(self, inputs, type_activation = 1):
        assert len(inputs) == len(self.weights - 1), "The length of input array " \
                                                 "doens't match with the len of " \
                                                 "weights array"
        sum = 0
        for i in range(0, len(inputs)):
            sum = sum + inputs[i] * self.weights[i]
        sum = sum + self.weights[len(self.weights)]  # BIAS

        # activation function
        if type_activation == 1:
            if sum > 1:
                return 1
            else:
                return 0
        else:
            return NotImplementedError

    def set_weights(self, w):
        self.weights = w

    def get_weights(self):
        return self.weights[:]  # this avoid loss of reference
