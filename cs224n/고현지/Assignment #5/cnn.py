#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

### YOUR CODE HERE for part 1i
import torch
import torch.nn as nn
import torch.nn.functional as F

# (-1, e_char, m_word)
class CNN(nn.Module):
    def __init__(self, e_char, f, m_word, k=5):
        """
        Init CNN which is a 1-D cnn.
        @param embed_size (int): embedding size of char (dimensionality)
        @param k: kernel size, also called window size
        @param f: number of filters, should be embed_size of word
        """

        super(CNN, self).__init__()
        self.conv1d = nn.Conv1d(in_channels=e_char, out_channels=f, kernel_size=k)
        self.maxpool = nn.MaxPool1d(kernel_size=m_word - k + 1)

    def forward(self, X_reshaped: torch.Tensor) -> torch.Tensor:
        """
        map from X_reshaped to X_conv_out
        @param X_reshaped (Tensor): Tensor of char-level embedding with shape (max_sentence_length,
                                    batch_size, e_char, m_word), where e_char = embed_size of char,
                                    m_word = max_word_length.
        @return X_conv_out (Tensor): Tensor of word-level embedding with shape (max_sentence_length,
                                    batch_size)
        """

        # x_conv shape : (batch_size, f, (m_word-k+1))
        X_conv = self.conv1d(X_reshaped)

        # x_conv_out_3d shape : (batch_size, f, 1)
        X_conv_out = self.maxpool(F.relu(X_conv))

        return torch.squeeze(X_conv_out, -1)

### END YOUR CODE

