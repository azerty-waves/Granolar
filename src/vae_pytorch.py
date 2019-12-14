#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import argparse
import os

from torchvision import datasets, transforms
from torchvision.utils import save_image

from src.vae import VAE


# get the arguments, if not on command line, the arguments are the default
parser = argparse.ArgumentParser(description='VAE MNIST Example')
parser.add_argument('--batch-size', type=int, default=128, metavar='N',
                    help='input batch size for training (default: 128)')
parser.add_argument('--epochs', type=int, default=10, metavar='N',
                    help='number of epochs to train (default: 10)')
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='enables CUDA training')
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                    help='how many batches to wait before logging training status')

args = parser.parse_args()





# loading the training dataset
train_dataset = datasets.MNIST('../data', train=True, download=True, transform=transforms.ToTensor())
    
# loading the test dataset
test_dataset = datasets.MNIST('../data', train=False, transform=transforms.ToTensor())


# main code
if __name__ == "__main__":
    if not os.path.exists('../results/'):
        os.makedirs('../results')
    vae = VAE(train_dataset, test_dataset, batch_size=args.batch_size, seed=args.seed, no_cuda=args.no_cuda)
    for epoch in range(args.epochs):
        vae.train()
        vae.test()
        sample = vae.create_sample()
        save_image(sample.view(64, 1, 28, 28), 'results/sample_' + str(epoch) + '.png')

