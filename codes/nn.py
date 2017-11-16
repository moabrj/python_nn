from neuron import neuron

class nn:

    def __init__(self, n_inputs, n_hidden_neurons, n_outputs):
        # the n_inputs + 1 is because of bias, which is present in this array
        self.hidden_layer = [neuron(0, n_inputs + 1) for x in range(n_hidden_neurons)]
        self.output_layer = [neuron(0, n_hidden_neurons) for x in range(n_outputs)]

    def compute_output(self, inputs):
        output_hidden_layer = []
        for i in range(len(self.hidden_layer)):
            output_hidden_layer[i] = self.hidden_layer[i].sum(inputs)

        output = []
        for i in range(len(self.output_layer)):
            output[i] = self.output_layer[i].sum(output_hidden_layer)

        return output