import torch
  1 import torch.nn as nn
  2 import torch.nn.functional as F
  3
  4 import torch.optim as optim
  5
  6 """Create Net"""
  7 class Net(nn.Module):
  8     def __init__(self):
  9         super(Net, self).__init__()
 10         """Kernel"""
 11         self.conv1 = nn.Conv2d(1, 6, 5)
 12         self.pool = nn. MaxPool2d(2, 2)
 13         self.conv2 = nn.Conv2d(6, 16, 5)
 14
 15         """Output"""
 16         self.fc1 = nn.Linear(16 * 5 * 5, 120)
 17         self.fc2 = nn.Linear(120, 84)
 18         self.fc3 = nn.Linear(84, 10)
 19
 20     def forward(self, x):
 21         x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
 22         x = F.max_pool2d(F.relu(self.conv2(x)), 2)
 23         x = x.view(-1, 16 * 5 * 5)
 24         x = F.relu(self.fc1(x))
 25         x = F.relu(self.fc2(x))
 26         x = self.fc3(x)
 27         return x
