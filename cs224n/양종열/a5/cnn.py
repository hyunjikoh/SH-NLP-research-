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
    """ Character-level Embedding에서 사용하는 1-d CNN
    """

    def __init__(self, in_channels, out_channels, kernel_size=5):
        """ Initialize 1D convolution for character embeddings.

        @param in_channels (int): input channel 갯수 (char embedding size, 50)
        @param out_channels (int): output channel 갯수 (word embedding size, 256)
        @param kernel_size (int): Convolution filter size (default: 5)
        """
        super(CNN, self).__init__()
        self.kernel_size = kernel_size
        self.conv = nn.Conv1d(in_channels=in_channels,
                              out_channels=out_channels,
                              kernel_size=kernel_size)
        self.max_pool = nn.AdaptiveMaxPool1d(output_size=1)
        # Adaptive pooling: https://titania7777.tistory.com/8

    def forward(self, x_reshaped: torch.Tensor) -> torch.Tensor:
        """ embeded words를 입력으로 받아 convolution 연산

        @param: x_reshaped (Tensor): character embeding, padding 을 거친 word의 list

        @return output (Tensor): 
        """
        # x_reshaped: (src_len * b, e_char, m_word)
        x_conv = self.conv(x_reshaped)
        # x_conv: (src_len * b, e_word, m_word - kernel_size + 1)
        # print(x_reshaped.shape, x_conv.shape)
        # embeding(channel) dimension 을 기준으로 max_pooling
        # (src_len * b, e_word, m_word - kernel_size + 1) 
        # -> ((src_len * b, e_word, 1))
        # -> ((src_len * b, e_word))
        x_conv_output = self.max_pool(F.relu(x_conv))
        # print(x_conv_output.shape)
        x_conv_output = x_conv_output.squeeze(dim=2)
        # x_conv_output: (src_len * b, e_word)
        return x_conv_output


### END YOUR CODE

