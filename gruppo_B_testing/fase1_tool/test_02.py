import torch

class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.layer(x)

def call_forward_directly():
    model = MyModel()
    output = model.forward(torch.randn(1, 10))
    return output
