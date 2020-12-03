# CS 224n: Assignment #5

## 1. Character-based convolutional encoder for NMT

(a) character의 vocab size가 word의 vocab size보다 더 작으므로 이를 표현하기 위한 embedding size도 더 작게 만드는게 합리적이다.

(b) Total number of parameter

- character-based embedding model

  $$ e_{char}, k, e_{word}, V_{word} $$

  1. Char Embeddings
    $$ V_{char} \times e_{char} = 96 \times 50 = 4,800 $$

  2. Convolutional Network

      - Weights:
        $$ f \times e_{char} \times k = e_{word} \times e_{char} \times k = 5 \times 256 \times 50 = 64,000 $$
      - bias:
        $$ f = e_{word} = 256 $$

  3. Highway Network
    $$ e_{word} \times e_{word} + e_word = 256 \ times 256 + 256 = 65,792 $$

  4. Total
    $$ 134,848 $$

- word embedding model
  $$ V_{word} \times e_{word} = 50,000 \times 256 = 2,800,000 $$

(c) Character Embeding을 할 때 CNN과 RNN의 비교

- CNN을 사용하면 주변 문자와의 관계를 n-gram과 같은 형태로 볼 수 있어 가까운 문자와의 관계를 형태소처럼 파악하는데 좋을 수 있다.
- RNN을 사용하면 주변 단어의 관계보다는 전체적인 흐름에 대한 관계를 배우기 때문에 형태에 따라 나뉠 수 있는 문자의 경우 CNN을 사용하는 것이 더 적합할 수 있다.

(d) Max-pooling vs Average-pooling

- Max-pooling: max-pooling은 윈도우의 가장 큰 값을 가져옴으로써 큰 값을 부각시키는데 요긴하다.
- Average-pooling: average-pooling은 윈도우의 평균 값을 가져옴으로써 전체적인 맥락을 가져오는데 요긴하다.
- 데이터에서 중요한 값을 추출하는데는 max-pooling이 전체적인 맥락 값을 가져오는데는 average-pooling이 좋을 수 있다.

## 2. Character-based LSTM decoder for NMT

(f)

```shell
> sh run.sh train
...
epoch 28, iter 184000, avg. loss 78.70, avg. ppl 110.18 cum. examples 63977, speed 6780.93 words/sec, time elapsed 17825.45 sec
epoch 28, iter 184000, cum. loss 84.66, cum. ppl 122.17 cum. examples 63977
begin validation ...
validation: iter 184000, dev. ppl 341.741448
hit patience 5
hit #5 trial
early stop!
```

```shell
> sh run.sh test
load test source sentences from [./en_es_data/test.es]
load test target sentences from [./en_es_data/test.en]
load model from model.bin
Decoding: 100% 8064/8064 [09:28<00:00, 14.17it/s]
Corpus BLEU: 24.300544859338885
```