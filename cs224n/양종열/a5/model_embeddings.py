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
        self.embed_char_size = 50  # $$ e_{char} $$
        self.embed_size = embed_size  # 256 $$ e_{word} $$

        self.char_embed = nn.Embedding(num_embeddings=len(vocab.char2id),
                                       embedding_dim=self.embed_char_size,
                                       padding_idx=pad_token_idx)
        self.cnn = CNN(in_channels=self.embed_char_size,
                       out_channels=self.embed_size)
        self.highway = Highway(size=self.embed_size)
        self.dropout = nn.Dropout(p=0.3)

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
        # 1. Record dimensions
        src_len, b, _e_char = input.shape

        # 2. character embedding
        # (src_len, b, m_word)
        # -> (src_len, b, m_word, e_char) 
        emb = self.char_embed(input)

        # 3. reshape
        # (src_len, b, m_word, e_char) 
        # -> (src_len*b, m_word, e_char) 
        # -> (src_len*b, e_char, m_word)
        embed_reshaped = emb.reshape(emb.size(0) * emb.size(1), emb.size(2), emb.size(3)).\
                             permute(0, 2, 1)

        # 4. cnn 
        # (src_len*b, e_char, m_word)
        # -> (src_len*b, e_word)
        conv_out = self.cnn(embed_reshaped)

        # 5. highway & dropout
        # (src_len*b, e_word)
        # -> (src_len*b, e_word)
        highway = self.highway(conv_out)
        word_emb = self.dropout(highway)

        # 6. reshape
        # (src_len*b, e_word)
        # -> (src_len, b, e_word)
        output = word_emb.reshape(src_len, b, word_emb.size(1))
        
        return output
        ### END YOUR CODE

