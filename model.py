from turtle import forward
from torch import nn
import torch.nn.functional as F
import torch

class SimpleCNN(nn.Module):

    def __init__(self, input_channels = 3, class_num = 10) -> None:
        super().__init__()

        self.conv_layer1 = nn.Conv2d(input_channels, 16, 5, 1)
        self.pool1 = nn.MaxPool2d(5, 1)
        self.conv_layer2 = nn.Conv2d(16, 16, 4, 1)
        self.pool2 = nn.MaxPool2d(3, 1)
        self.conv_layer3 = nn.Conv2d(16, 32, 4, 1)
        self.conv_layer4 = nn.Conv2d(32, 32, 4, 1)
        self.conv_layer5 = nn.Conv2d(32, 32, 4, 1)

        self.linear1 = nn.Linear(32*10*10, 8*10*10)
        self.linear2 = nn.Linear(8*10*10, 2*10*10)
        self.linear3 = nn.Linear(200, 50)
        self.linear4 = nn.Linear(50, class_num)
        self.linear5 = nn.Linear(class_num, class_num)
    
    def forward(self, X):
        conv_output = self.pool1(F.relu(self.conv_layer1(X)))
        conv_output = self.pool2(F.relu(self.conv_layer2(conv_output)))
        conv_output = F.relu(self.conv_layer3(conv_output))
        conv_output = F.relu(self.conv_layer4(conv_output))
        conv_output = F.relu(self.conv_layer5(conv_output))
        
        vec_output = nn.Flatten()(conv_output)
        vec_output = F.relu(self.linear1(vec_output))
        vec_output = F.relu(self.linear2(vec_output))
        vec_output = F.relu(self.linear3(vec_output))
        vec_output = F.relu(self.linear4(vec_output))
        vec_output = F.relu(self.linear5(vec_output))
        return vec_output
        
