

class neuron:

    weights = 0

    def __init__(cls):
        cls.weights = 0
        cls.BIAS = 0
        pass

    def sum(cls, inputs, type_activation=1):
        assert len(inputs) == len(cls.weights), "The length of input array " \
                                                 "doens't match with the len of " \
                                                 "weights array"
        sum = 0
        for i in range(0, len(inputs)):
            sum = sum + inputs[i] * cls.weights[i]
        sum = sum + cls.BIAS

        # activation function
        if type_activation == 1:
            if sum > 1:
                return 1
            else:
                return 0
        else:
            return NotImplementedError

    def set_weights(cls, w):
        cls.weights = w

    def get_weights(cls):
        return cls.weights[:]  # this avoid loss of reference
