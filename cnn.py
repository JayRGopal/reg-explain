from torch import nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    """
    Class representing convolutional neural network through the PyTorch DL framework
    """

    def __init__(self, input_channels = 3, class_num = 10) -> None:
        """
        Initializes convolutional layers, pooling layers, and linear layers for
        the SimpleCNN class. Inherits from nn.Module initializer function.
        :param input_channels: number of color channels. Default 3 for RGB
        :param class_num: number of classes that will be predicted by the model.
            Default 10 for the 10 classes represented by CIFAR10
        """

        super().__init__()

        # self.conv_layer1 = nn.Conv2d(input_channels, 16, 4, 1)
        # self.pool1 = nn.MaxPool2d(3, 2)
        # self.conv_layer2 = nn.Conv2d(16, 16, 4, 1)
        # self.pool2 = nn.MaxPool2d(3, 1)
        # self.conv_layer3 = nn.Conv2d(16, 32, 3, 1)
        # self.conv_layer4 = nn.Conv2d(32,64, 3, 1)

        # self.linear1 = nn.Linear(64*5*5, 32*5*5)
        # self.linear2 = nn.Linear(32*5*5, 16*6*6)
        # self.linear3 = nn.Linear(16*6*6, 8*6*6)
        # self.linear4 = nn.Linear(8*6*6, 144)
        # self.linear5 = nn.Linear(144, 50)
        # self.linear6 = nn.Linear(50, class_num)
        # self.linear7 = nn.Linear(class_num, class_num)

        self.conv_layer1 = nn.Conv2d(input_channels, 16, 8, 1)
        self.conv_layer2 = nn.Conv2d(16, 16, 5, 1)
        self.conv_layer3 = nn.Conv2d(16, 32, 3, 1)
        self.pool1 = nn.MaxPool2d(4, 2)

        self.linear1 = nn.Linear(2048, 524)
        self.linear2 = nn.Linear(524, 128)
        self.linear3 = nn.Linear(128, class_num)
    
    def forward(self, X):
        """
        Performs forward propagation through the defined CNN layers for given input
        :param X: Input to the CNN network. Dimension (batch size, 3 , 32, 32)
        :return: (batch size, 10) torch tensor output of convolution and 
        subsequent linear layers. Size 10 given the 10 predicted classes.
        """
        
        # Pass through convolutional layers, with relu activation
        conv_output = F.gelu(self.conv_layer1(X))
        conv_output = F.gelu(self.conv_layer2(conv_output))
        conv_output = self.pool1(F.gelu(self.conv_layer3(conv_output)))
        
        # Pass through linear layers.
        # GELU for every layer except last. Softmax for the last layer.
        vec_output = nn.Flatten()(conv_output)
        vec_output = F.gelu(self.linear1(vec_output))
        vec_output = F.gelu(self.linear2(vec_output))
        vec_output = self.linear3(vec_output)
        return vec_output
    
    