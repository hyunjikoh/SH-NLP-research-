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
    """ Character-level Embedding에서 사용하는 Highway Network
    output = gate * h + (1-gate) * h
    """

    def __init__(self, size):
        """ Highway Netowrk 초기화

        @param size (int): hidden layer의 input/output size
        """
        super(Highway, self).__init__()
        self.gate = nn.Linear(size, size)
        self.proj = nn.Linear(size, size)
    
    def forward(self, input: torch.Tensor) -> torch.Tensor:
        """ convolution에서 나온 출력값을 입력으로 받아 highway network 연산

        @param input (Tensor): convolution output (src_len * b, e_word)

        @return highway (Tensor): highway output (src_len * b, e_word)

        """
        src_len_b, e_word = input.shape
        proj = F.relu(self.proj(input))
        assert proj.shape == (src_len_b, e_word)
        gate = torch.sigmoid(self.gate(input))
        assert gate.shape == (src_len_b, e_word)
        highway = gate * proj + (1 - gate) * input
        assert highway.shape == (src_len_b, e_word)
        return highway

### END YOUR CODE 

