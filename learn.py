net = Net()

#Note that the input has to be 32 by 32 matrix in this net system
# input = torch.randn(1, 1, 32, 32)
# target = torch.randn(1)
# target = target.view(1, -1)

#Create Loss Optimizer(SGD)
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
criterion = nn.MSELoss()



    
# Learning Loop
for line in range(60):
    #Zero the grad buffers(Initializing)
    optimizer.zero_grad()
    
    inTens, targetTens = dataToTens(line)
    outTens = net(inTens)
    
    loss = criterion(outTens, targetTens)
    loss.backward()

    #Update
    optimizer.step()

    #test
#     print(net.conv1.bias.grad)
