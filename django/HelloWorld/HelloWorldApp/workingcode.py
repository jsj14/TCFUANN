
# coding: utf-8

# In[1]:

import json
with open('jsondataindia.json') as datafile:
    data =json.load(datafile)
import numpy as np
temp = []
for index in range(0,52):
  temp.append(data[index]["COAL "])
x_train =np.array(temp)
x_train=x_train.reshape((52,1))
y=[]
for index in range(0,52):
  y.append(data[index]["NATURAL GAS"])
temp = np.array(y)
temp=temp.reshape((52,1))
x_train= np.column_stack((x_train, temp))
y=[]
for index in range(0,52):
  y.append(data[index]["GLOBAL OIL"])
temp = np.array(y)
temp=temp.reshape((52,1))
x_train=np.column_stack((x_train, temp))
y=[]
for index in range(0,52):
  y.append(data[index]["PRIMARY CONSUMPTION"])
temp = np.array(y)
temp=temp.reshape((52,1))
x_train=np.column_stack((x_train, temp))
y=[]
for index in range(0,52):
  y.append(data[index]["AVG CO2 EMISSIONS"])
temp = np.array(y)
temp=temp.reshape((52,1))
y_train=temp
i=0
base = min(y_train)
range = max(y_train) - base
for x in y_train:
    x = (x-base)/range
    y_train[i]=x
    i=i+1
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0 - x**2

class NeuralNetwork:
    def __init__(self, layers, activation='sigmoid'):
        if activation == 'sigmoid':
            self.activation = sigmoid
            self.activation_prime = sigmoid_prime
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_prime = tanh_prime

        # Set weights
        self.weights = []
        # layers = [2,2,1]
        # range of weight values (-1,1)
        # input and hidden layers - random((2+1, 2+1)) : 3 x 3
        for i in range(1, len(layers) - 1):
            r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
            self.weights.append(r)
            # output layer - random((2+1, 1)) : 3 x 1
            r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
            self.weights.append(r)
    def fit(self, X, y, learning_rate=0.2, epochs=100000):
        # Add column of ones to X
        # This is to add the bias unit to the input layer
        ones = np.atleast_2d(np.ones(X.shape[0]))
        X = np.concatenate((ones.T, X), axis=1)
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.weights)):
                    dot_value = np.dot(a[l], self.weights[l])
                    activation = self.activation(dot_value)
                    a.append(activation)
            # output layer
            error = y[i] - a[-1]
            deltas = [error * self.activation_prime(a[-1])]

            # we need to begin at the second to last layer 
            # (a layer before the output layer)
            for l in range(len(a) - 2, 0, -1): 
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))

            # reverse
            # [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
            deltas.reverse()

            # backpropagation
            # 1. Multiply its output delta and input activation 
            #    to get the gradient of the weight.
            # 2. Subtract a ratio (percentage) of the gradient from the weight.
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)
            if k % 10000 == 0: print 'epochs:', k

    def predict(self, x): 
        a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)   
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a

if __name__ == '__main__':
    nn = NeuralNetwork([4,5,1])
    X = x_train
    y = y_train
    nn.fit(X, y)
    for e in X:
        print(nn.predict(e))
            


# In[2]:

y_train


# In[ ]:



