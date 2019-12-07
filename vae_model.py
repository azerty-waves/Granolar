# -*- coding: utf-8 -*-

import torch
from torch import nn, optim
from torch.nn import functional

# definition of beta, should be 0 < beta < 1
# (this needs to be changed though, could be + pretty if passed as arg)

beta = 0.5


class VAE_Model(nn.Module):
    def __init__(self):
        super(VAE_Model, self).__init__()

        self.fc1 = nn.Linear(784, 400)
        self.fc21 = nn.Linear(400, 20)
        self.fc22 = nn.Linear(400, 20)
        self.fc3 = nn.Linear(20, 400)
        self.fc4 = nn.Linear(400, 784)

    def encode(self, x):
        h1 = functional.relu(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5*logvar)
        eps = torch.randn_like(std)
        return mu + beta*eps*std

    def decode(self, z):
        h3 = functional.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h3))

    def forward(self, x):
        mu, logvar = self.encode(x.view(-1, 784))
        z = self.reparameterize(mu, logvar)
        return self.decode(z), mu, logvar
