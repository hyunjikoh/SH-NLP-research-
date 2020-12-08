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
import torch
import torch.nn as nn

# Do not change these imports; your module names should be
#   `CNN` in the file `cnn.py`
#   `Highway` in the file `highway.py`
# Uncomment the following two imports once you're ready to run part 1(j)

# from cnn import CNN
# from highway import Highway
from cnn import CNN
from highway import Highway

# End "do not change" 

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
        self.e_char = 50
        self.w_word = 21
        self.char_embedding = nn.Embedding(len(vocab.char2id), self.e_char, pad_token_idx)
        # f = embed_size
        self.convNN = CNN(self.e_char, self.embed_size, self.w_word)
        self.highway = Highway(embed_size=self.embed_size)

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

        # sanity_check 1j
        # sentence_length = 10, BATCH_SIZE = 5, m_word = 21, e_char = 50
        # src_len, b, _ = input.shape

        # Tensor: (sentence_length, batch_size, m_word, e_char)
        emb = self.char_embedding(input)
        print(emb.shape) # torch.Size([10, 5, 21, 50])

        # Tensor : (sentence_length, batch_size, e_char, m_word)
        x_reshape_4D = emb.permute(0, 1, 3, 2)
        print(x_reshape_4D.shape) # torch.Size([10, 5, 50, 21])

        sentence_length, batch_size, e_word, m_word = x_reshape_4D.shape

        # Tensor : (f, e_char, m_word)
        x_reshape = x_reshape_4D.view(-1, e_word, m_word)
        print(x_reshape.shape) # torch.Size([50, 50, 21])

        # Tensor : (-1, e_word)
        conv_out = self.convNN(x_reshape)
        print(conv_out.shape) # torch.Size([50, 3])


        word_emb = self.highway(conv_out)  # Tensor: (src_len * b, e_word)

        # 5. Reshape word embeddings to expected output shape.
        output = word_emb.reshape(sentence_length, batch_size, word_emb.size(1))  # Tensor: (src_len, b, e_word)

        return output

        ### END YOUR CODE

