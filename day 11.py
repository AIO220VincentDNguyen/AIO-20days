import torch
import torch.nn as nn
import torch.nn.functional as F

# class ReLUActivateFunction inheritance from nn.Module
class ReLUActivateFunction(nn.Module):
    def __init__(self):
        super(ReLUActivateFunction, self).__init__()

    def forward(self, x):
        return torch.relu(x)

# class SigmoidActivateFunction inheritance from nn.Module
class SigmoidActivateFunction(nn.Module):
    def __init__(self):
        super(SigmoidActivateFunction, self).__init__()

    def forward(self, x):
        return torch.sigmoid(x)

# create object
relu = ReLUActivateFunction()
sigmoid = SigmoidActivateFunction()

# create tensor
x = torch.tensor([1, -5, 1.5, 2.7, -5], dtype=torch.float32)

# apply action function
relu_result = relu(x)
sigmoid_result = sigmoid(x)


print(f'ReLU: {relu_result}')
print(f'Sigmoid: {sigmoid_result}')
