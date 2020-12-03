#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

### YOUR CODE HERE for part 1i

import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):
    """ Convolutional Neural Network for Character-level Embedding.
    """

    def __init__(self, in_channels, out_channels, kernel_size=5):
        """ Initialize 1D convolution for character embeddings.

        @param in_channels (int): 
        @param out_channels (int): 
        @param kernel_size (int): 
        """
        super(CNN, self).__init__()
        self.conv = nn.Conv1d(in_channels=in_channels,
                              out_channels=out_channels,
                              kernel_size=kernel_size)
        self.max_pool = nn.AdaptiveMaxPool1d(output_size=1)

    def forward(self, embed_words: torch.Tensor) -> torch.Tensor:
        """ take list of embeded words, compute convolution

        @param: embed_words (Tensor):

        @return output (Tensor): 
        """
        h = F.relu(self.conv(embed_words))
        # (src_len * b, e_word)
        output = self.max_pool(h).squeeze(dim=2)
        return output


### END YOUR CODE

