#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

### YOUR CODE HERE for part 1h

import torch
import torch.nn as nn
import torch.nn.functional as F

class Highway(nn.Module):
    """ Highway Network for Character-level Embedding
    """

    def __init__(self, size):
        """ Init Highway Netowrk

        @param size (int): size if feature dimention of input/output
        """
        super(Highway, self).__init__()
        self.gate = nn.Linear(size, size)
        self.proj = nn.Linear(size, size)
    
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        """ Take a convolution output, compute highway network output

        @param input (Tensor): convolution output (src_len * b, e_word)

        @return highway (Tensor): highway output (src_len * b, e_word)

        """
        proj = F.relu(self.proj(input))
        gate = torch.sigmoid(self.gate(input))
        highway = gate * proj + (1 - gate) * input
        return highway

### END YOUR CODE 

