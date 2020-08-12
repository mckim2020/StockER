import torch
import torch.nn as nn
import torch.nn.functional as F

import torch.optim as optim

"""Create Net"""
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        """Kernel"""
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn. MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)

        """Output"""
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

     """ num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
    """


net = Net()
"""Note that the input has to be 32 by 32 matrix in this net system"""
input = torch.randn(1, 1, 32, 32)
target = torch.randn(10)
target = target.view(1, -1)

"""Create Loss Optimizer(SGD)"""
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
criterion = nn.MSELoss()


  
"""Code under has to be implemented inside training loop"""

"""Zero the grad buffers(Initializing)"""
optimizer.zero_grad()
output = net(input)
loss = criterion(output, target)
loss.backward()

"""Update"""
optimizer.step()

"""test"""
print(net.conv1.bias.grad)

"""
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)

print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

params = list(net.parameters())
print(len(params))
"""

