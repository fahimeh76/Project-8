import math
import random

class NeuralNetworks():
    def __init__(self):
        self.wights = [random.uniform(-1,1),random.uniform(-1,1), random.uniform(-1,1)]

    #predict the output
    def think(self):
        sum_of_weighted_inputs = self.__sum_of_weighted_inputs(neuron_inputs)
        neuron_output = self.__sigmoid()
        return neuron_output

    #adjust the weight to minimize the error
    def train(self, training_set_examples, number_of_iteration = 10000):
        for iteration in number_of_iteration:
            for training_set_example in training_set_examples:

                #predict the output:
                predictade_output = self.think(training_set_example["inputs"])

                #calculate error:
                error_in_output = training_set_example["output"] - predictade_output

                #iterate and adjust:
                for index in range(len(self.weight)):
                    neuron_input = training_set_example["inputs"][index]

                    adjust_weight = neuron_input* error_in_output * self.__sigmoid_gradient(predictade_output)

                    self.weights[index] += adjust_weight



        

    def __sigmoid(self, sum_of_weighted_inputs):
        return 1/(1+math.exp(-sum_of_weighted_inputs))

    def __sigmoid_gradient(self, neuron_output):
        return neuron_output*(1-neuron_output)

    def __sum_of_weighted_inputs(self, neuron_inputs):
        sum_of_weighted_inputs = 0

        for index, neuron_input in enumerate(neuron_inputs):
            sum_of_weighted_inputs+= self.weights[index]* neuron_input
            return sum_of_weighted_inputs



training_set_examples = [{"inputs": [0,0,1], "outputs":0},
                        {"inputs": [1,1,1], "outputs":1},
                        {"inputs": [1,0,1], "outputs":1},
                        {"inputs": [0,1,1], "outputs":0}
                         ]
neural_network = NeuralNetworks()
print("random weights are {}".format(str(neural_network.wights)))

neural_network.train(training_set_examples, 10000)
print("final  weights are {}".format(str(neural_network.wights)))

new_situation = [1,0,0]
prediction = neural_network.think(new_situation)

print("The result for predicting [1,0,0] is: {}".format(prediction ))

