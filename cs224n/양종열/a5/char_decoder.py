#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CS224N 2018-19: Homework 5
"""

import torch
import torch.nn as nn

class CharDecoder(nn.Module):
    def __init__(self, hidden_size, char_embedding_size=50, target_vocab=None):
        """ Init Character Decoder.

        @param hidden_size (int): Hidden size of the decoder LSTM
        @param char_embedding_size (int): dimensionality of character embeddings
        @param target_vocab (VocabEntry): vocabulary for the target language. See vocab.py for documentation.
        """
        ### YOUR CODE HERE for part 2a
        ### TODO - Initialize as an nn.Module.
        ###      - Initialize the following variables:
        ###        self.charDecoder: LSTM. Please use nn.LSTM() to construct this.
        ###        self.char_output_projection: Linear layer, called W_{dec} and b_{dec} in the PDF
        ###        self.decoderCharEmb: Embedding matrix of character embeddings
        ###        self.target_vocab: vocabulary for the target language
        ###
        ### Hint: - Use target_vocab.char2id to access the character vocabulary for the target language.
        ###       - Set the padding_idx argument of the embedding matrix.
        ###       - Create a new Embedding layer. Do not reuse embeddings created in Part 1 of this assignment.
        super(CharDecoder, self).__init__()
        self.charDecoder = nn.LSTM(input_size=char_embedding_size, hidden_size=hidden_size)
        self.char_output_projection = nn.Linear(in_features=hidden_size,
                                                out_features=len(target_vocab.char2id))
        self.decoderCharEmb = nn.Embedding(num_embeddings=len(target_vocab.char2id),
                                             embedding_dim=char_embedding_size,
                                             padding_idx=target_vocab.char2id['<pad>'])
        self.target_vocab = target_vocab

        ### END YOUR CODE

    
    def forward(self, input, dec_hidden=None):
        """ Forward pass of character decoder.

        @param input: tensor of integers, shape (length, batch)
        @param dec_hidden: internal state of the LSTM before reading the input characters. A tuple of two tensors of shape (1, batch, hidden_size)

        @returns scores: called s_t in the PDF, shape (length, batch, self.vocab_size)
        @returns dec_hidden: internal state of the LSTM after reading the input characters. A tuple of two tensors of shape (1, batch, hidden_size)
        """
        ### YOUR CODE HERE for part 2b
        ### TODO - Implement the forward pass of the character decoder.
        
        # 1. input character embeding 
        # (length, batch) -> (length, batch, char_embedding_size)
        char_embeds = self.decoderCharEmb(input)

        # 2. character embeding LSTM layer
        # (length, batch, hidden_size), ((1, batch, hidden_size), (1, batch, hidden_size)) = LSTM()
        output, dec_hidden = self.charDecoder(char_embeds, dec_hidden)

        # 3. output projection (length, batch, vocab_size)
        scores = self.char_output_projection(output)

        return scores, dec_hidden
        
        ### END YOUR CODE 


    def train_forward(self, char_sequence, dec_hidden=None):
        """ Forward computation during training.

        @param char_sequence: tensor of integers, shape (length, batch). Note that "length" here and in forward() need not be the same.
        @param dec_hidden: initial internal state of the LSTM, obtained from the output of the word-level decoder. A tuple of two tensors of shape (1, batch, hidden_size)

        @returns The cross-entropy loss, computed as the *sum* of cross-entropy losses of all the words in the batch.
        """
        ### YOUR CODE HERE for part 2c
        ### TODO - Implement training forward pass.
        ###
        ### Hint: - Make sure padding characters do not contribute to the cross-entropy loss.
        ###       - char_sequence corresponds to the sequence x_1 ... x_{n+1} from the handout (e.g., <START>,m,u,s,i,c,<END>).

        # 1. probability 계산
        input = char_sequence[:-1]  # remove <END>
        scores, _dec_hidden = self.forward(input, dec_hidden)
        scores = scores.permute(1, 2, 0)  # (batch, vocab_size, length)

        # 2. loss 계산
        target = char_sequence[1:].permute(1, 0)  # remove <START> and permute (batch, length)
        # CrossEntropyLoss: This criterion combines nn.LogSoftmax() and nn.NLLLoss() in one single class.
        loss_char_dec = nn.CrossEntropyLoss(reduction='sum')
        loss = loss_char_dec(scores, target)

        return loss
        ### END YOUR CODE

    def decode_greedy(self, initialStates, device, max_length=21):
        """ Greedy decoding
        @param initialStates: initial internal state of the LSTM, a tuple of two tensors of size (1, batch, hidden_size)
        @param device: torch.device (indicates whether the model is on CPU or GPU)
        @param max_length: maximum length of words to decode

        @returns decodedWords: a list (of length batch) of strings, each of which has length <= max_length.
                              The decoded strings should NOT contain the start-of-word and end-of-word characters.
        """

        ### YOUR CODE HERE for part 2d
        ### TODO - Implement greedy decoding.
        ### Hints:
        ###      - Use target_vocab.char2id and target_vocab.id2char to convert between integers and characters
        ###      - Use torch.tensor(..., device=device) to turn a list of character indices into a tensor.
        ###      - We use curly brackets as start-of-word and end-of-word characters. That is, use the character '{' for <START> and '}' for <END>.
        ###        Their indices are self.target_vocab.start_of_word and self.target_vocab.end_of_word, respectively.
        
        # 1. Record shape
        _1, batch_size, _hidden_size = initialStates[0].shape
        START, END = self.target_vocab.start_of_word, self.target_vocab.end_of_word

        # 2. Initialize variable
        output_words = [""] * batch_size
        start_char_ids = [[START] * batch_size]
        current_char_ids = torch.tensor(start_char_ids, device=device)

        current_states = initialStates

        # 모든 word에 대해 character 단위로 순서대로 연산 (1, batch)
        for _ in range(max_length):
            # current_char_ids: (1, batch)
            scores, current_states = self.forward(current_char_ids, current_states)
            # scores: (1, batch, vocab_size)
            probabilities = torch.softmax(scores.squeeze(0), dim=1)  
            # probabilities: (batch, vocab_size)
            current_char_ids = torch.argmax(probabilities, dim=1).unsqueeze(0)
            # current_char_ids: (1, batch)
            # batch 에 대해 연산 한 character씩 연산
            for i, c in enumerate(current_char_ids.squeeze(dim=0)):
                output_words[i] += self.target_vocab.id2char[int(c)]

        # <END> 까지의 문자 취합
        decodeWords = []
        for word in output_words:
            end_pos = word.find(self.target_vocab.id2char[END])
            decodeWords.append(word if end_pos == -1 else word[:end_pos])
        return decodeWords
        
        ### END YOUR CODE

