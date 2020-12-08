#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
model_embeddings.py: Embeddings for the NMT model
Pencheng Yin <pcyin@cs.cmu.edu>
Sahil Chopra <schopra8@stanford.edu>
Anand Dhoot <anandd@stanford.edu>
Michael Hahn <mhahn2@stanford.edu>
"""

import torch.nn as nn

# Do not change these imports; your module names should be
#   `CNN` in the file `cnn.py`
#   `Highway` in the file `highway.py`
# Uncomment the following two imports once you're ready to run part 1(j)

# from cnn import CNN
# from highway import Highway

# End "do not change" 

import torch
from torch import nn

from cnn import cnn
from highway import HighwayNet


class ModelEmbeddings(nn.Module):
    """
    Class that converts input words to their CNN-based embeddings.
    """
    def __init__(self, embed_size, vocab):
        """
        Init the Embedding layer for one language
        @param embed_size (int): Embedding size (dimensionality) for the output 
        @param vocab (VocabEntry): VocabEntry object. See vocab.py for documentation.
        """
        super(ModelEmbeddings, self).__init__()

        ## A4 code
        # pad_token_idx = vocab.src['<pad>']
        # self.embeddings = nn.Embedding(len(vocab.src), embed_size, padding_idx=pad_token_idx)
        ## End A4 code

        ### YOUR CODE HERE for part 1j
        pad_token_idx = vocab.char2id['<pad>']
        self.embed_size = embed_size
        char_embed_size = 50
        self.char_embedding = nn.Embedding(len(vocab.char2id), char_embed_size, pad_token_idx)
        self.myCnn = cnn(feature=self.embed_size)
        self.highway = HighwayNet(embed_size=self.embed_size)
        self.dropout = nn.Dropout(0.3)

        ### END YOUR CODE

    def forward(self, input):
        """
        Looks up character-based CNN embeddings for the words in a batch of sentences.
        @param input: Tensor of integers of shape (sentence_length, batch_size, max_word_length) where
            each integer is an index into the character vocabulary

        @param output: Tensor of shape (sentence_length, batch_size, embed_size), containing the 
            CNN-based embeddings for each word of the sentences in the batch
        """
        ## A4 code
        # output = self.embeddings(input)
        # return output
        ## End A4 code

        ### YOUR CODE HERE for part 1j
        x_word_emb_list = []
        for x_padded in input:      # input : (sentence_length, batch_size, max_word_length)
            # x_padded : (batch_size, max_word_length)
            x_emb = self.char_embedding(x_padded)   # x_emb : (batch_size, max_word_length, char_embed_size)
            x_reshaped = x_emb.permute(0, 2, 1)     # x_reshape : (batch_size, char_embed_size, max_word_length)
            x_conv_out = self.myCnn(x_reshaped)     # x_conv_out : (batch_size, feature)
            x_highway = self.highway(x_conv_out)
            x_word_emb = self.dropout(x_highway)
            x_word_emb_list.append(x_word_emb)

        x_word_emb = torch.stack(x_word_emb_list)       # x_word_emb : (sentence_length, batch_size, feature)
        return x_word_emb
        ### END YOUR CODE

