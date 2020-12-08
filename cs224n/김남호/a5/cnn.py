#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

import torch
from torch import nn

### YOUR CODE HERE for part 1i
class cnn(nn.Module):
    def __init__(self, embed_size=50, max_word=21, kernel_size=5, feature=None):
        super(cnn, self).__init__()

        self.conv1d = nn.Conv1d(in_channels=embed_size, out_channels=feature, kernel_size=kernel_size)
        self.maxpool = nn.MaxPool1d(max_word-kernel_size+1)     # max_word - kernel_size + 1

    def forward(self, x_reshape):
        # x_reshape : (batch_size, char_embed_size, max_word_length)
        x_conv = self.conv1d(x_reshape)     # x_conv : (batch_size, feature, conv_out_size)
        x_conv_out = self.maxpool(nn.functional.relu(x_conv))   # x_conv_out : (batch_size, feature, 1)
        return torch.squeeze(x_conv_out, -1)    # (batch_size, feature)
### END YOUR CODE