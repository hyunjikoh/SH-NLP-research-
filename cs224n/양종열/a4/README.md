# NMT Assignment

## 1. Neural Machine Translation with RNNs

### (g) mask

mask를 1로 지정하면 attention distribution 값을 -inf로 설정해준다. -inf로 설정된 값들은 softmax 계산시 0으로 설정되고 attention distribution이 0으로 설정되면 그 값들은 value값을 가져오지 않는다. attention에 mask를 씌워주는 것은 실제 입력 단어가 없는 값(padding된 값)으로부터 값을 가져오지 않기 위함이다.

### (i) run test

```bash
sh run.sh test

load test source sentences from [/content/drive/My Drive/study/CS224N/assignment/a4/en_es_data/test.es]
load test target sentences from [/content/drive/My Drive/study/CS224N/assignment/a4/en_es_data/test.en]
load model from /content/drive/My Drive/study/CS224N/assignment/a4/model.bin
5 70
Decoding: 100%|██████████| 8064/8064 [07:24<00:00, 18.13it/s]
Corpus BLEU: 22.68303981369953
```

### (j) attention 비교

- Dot Product
  - Advantage: vector간의 similarity를 직관적으로 구할 수 있다. 연산이 효율적이다.
  - Disadvantage: 별도의 학습 파라메터가 없어 유연하지 않다.

- Additive:
  - Advantage: 벡터별로 학습 파라메터가 있고 activation 함수를 포함하고 있어 매우 유연하다. 복잡한 패턴의 attention을 학습할 수 있다.
  - Disadvantage: 연산이 오래 걸리고 학습하는데에 시간이 오래 걸린다.

## 2. Analyzing NMT Systems

### (a) check test results

- i. Here's -> So, favorite -> one
- ii.
- iii. \<unk\> -> Bolingbroke
- v. women's room -> teachers' lounge
- vi.
  - 100,000 -> 250,000

### (b) Fine error

### (c) BLEU score

- i

  Source Sentence s: el amor todo lo puede

  Reference Translation r1: love can always find a way

  Reference Translation r2: love makes anything possible

  NMT Translation c1: the love can always do

  NMT Translation c2: love can make anything possible

  - c1: the love can always do
    $$ p_1 = \frac{3}{5} $$
    $$ p_2 = \frac{2}{4} $$
    $$ BP = 1 $$
    $$ BLEU = 1 * exp (0.5log(3/5) + 0.5log(2/4)) = 0.76994 $$

  - c2: love can make anything possible
    $$ p_1 = \frac{4}{5} $$
    $$ p_2 = \frac{2}{4} $$
    $$ BP = 1 $$
    $$ BLEU = 1 * exp (0.5log(4/5) + 0.5log(2/4)) = 0.81957 $$

  - c2 가 BLEU score가 더 높고 reference와 비교해보면 c2가 더 잘 된듯 함

- ii.
  - c1: the love can always do
    $$ p_1 = \frac{3}{5} $$
    $$ p_2 = \frac{2}{4} $$
    $$ BP = 1 $$
    $$ BLEU = 1 * exp (0.5log(3/5) + 0.5log(2/4)) = 0.76994 $$

  - c2: love can make anything possible
    $$ p_1 = \frac{2}{5} $$
    $$ p_2 = \frac{1}{4} $$
    $$ BP = 1 $$
    $$ BLEU = 1 * exp (0.5log(2/5) + 0.5log(1/4)) = 0.60653 $$

  - c1 가 BLEU score가 더 높게 나옴.

- iii.
  - 한 문장이 여러가지 방식으로 표현될 수 있는데 여러 문장과 비교함으로써 이를 보완해주는 듯 함. 하나의 문장과 비교할 경우 의역이 아닌 직역이 잘 된 문장 점수가 높게 나올 수 있음

- iv.
  - Advantages:
    성능을 빠르게 수치화할 수 있음
  - Disadvantages:
    단순히 단어가 매칭된 것을 비교하기 때문에함 reference와 다른 어휘로 표현할 경우 점수가 낮을 수 있음
