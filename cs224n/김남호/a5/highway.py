#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

import torch
from torch import nn

### YOUR CODE HERE for part 1h
class HighwayNet(nn.Module):
    def __init__(self, embed_size):
        super(HighwayNet, self).__init__()

        self.projection = nn.Linear(embed_size, embed_size)
        self.gate = nn.Linear(embed_size, embed_size)

    def forward(self, x):
        x_projection = nn.functional.relu(self.projection(x))
        x_gate = torch.sigmoid(self.gate(x))
        x_highway = (x_projection * x_gate) + (x * (1-x_gate))
        return x_highway
        # x_highway = torch.mul(x_projection, x_gate) + torch.mul(x, 1-x_gate)
        #x_word_emb = self.dropout(x_highway)

        ### END YOUR CODE