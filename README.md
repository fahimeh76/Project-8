Neural Network Implementation:
This Python code implements a simple neural network that utilizes a basic feedforward structure with a sigmoid activation function and the gradient descent optimization technique for training. The neural network is designed to learn from a given training dataset, adjust its weights over multiple iterations, and make predictions based on new input data.
Features:
•	Random Initialization of Weights: At the start of the program, the neural network initializes weights randomly between -1 and 1.
•	Sigmoid Activation Function: The neural network uses the sigmoid function as an activation function to determine the output of the neuron after processing the weighted sum of the inputs.
•	Training Process: The network is trained using a set of training examples, which consist of inputs and corresponding outputs. During the training process, the network adjusts its weights by computing the error (the difference between the predicted output and the actual output) and applying gradient descent. This training continues for a specified number of iterations (default is 10,000 iterations).
•	Error Minimization: The weights are updated iteratively to minimize the error in the predicted output by calculating the gradient of the sigmoid function and adjusting the weights accordingly.
•	Prediction: After the training is complete, the network can predict the output for new input data by applying the learned weights and running the inputs through the activation function.
Components:
•	think(): This method computes the weighted sum of inputs, applies the sigmoid activation, and returns the predicted output.
•	train(): This method iterates through the training dataset, predicts the output, calculates the error, and adjusts the weights using the sigmoid gradient.
•	__sigmoid(): The activation function used in the neural network to calculate the output of the neuron.
•	__sigmoid_gradient(): The gradient of the sigmoid function used to adjust the weights during the training process.
•	__sum_of_weighted_inputs(): This method computes the sum of the product of each input and its corresponding weight.
![image](https://github.com/user-attachments/assets/95f7ff34-e882-48e3-ba85-1618aa530291)
