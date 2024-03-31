
import torch.nn as nn

class Softmax(nn.Module):

    def __init__(self, in_size, out_size):

        super(Softmax, self).__init__()

        self.linear = nn.Linear(in_size, out_size)

    def forward(self, x):

        out = self.linear(x)

        return out