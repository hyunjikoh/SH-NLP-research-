# Dependency Parsing

## 1. Machine Learning & Neural Networks

### (a) Adam Optimizer

#### i. minibatch의 gradient값이 일시적으로 잘못되더라도 올바른 방향으로 갈 수 있도록 유도해줌

#### ii. gradient가 큰 값을 줄여주고 작은 값을 키워줌. 일종의 normalization 효과?

### (b) Dropout

#### i. (1-$p_{drop}$)만큼 값을 키워줘야 한다. $\gamma = \frac{1}{1-p_{drop}}$

#### ii. Training때 다양한 노드가 생성된 Neural Network로 학습하고 test때 이를 모두 융합해줌으로써 일종의 ensemble효과를 줄 수 있다.

## 2. Neural Transition-Based Dependency Parsing

### (a)

| Stack  | Buffer  | New dependency  | Transition  |
|---|---|---|---|
|[ROOT]   | [I, parsed, this, sentence, correctly]  |   | Initial Configuration  |
|[ROOT, I]   | [parsed, this, sentence, correctly]  |   | SHIFT  |
|[ROOT, I, parsed]   | [this, sentence, correctly]  |   | SHIFT  |
|[ROOT, parsed] | [this, sentence, correctly] | parsed -> I | LEFT-ARC |
|[ROOT, parsed, this] | [sentence, correctly] |  | SHIFT |
|[ROOT, parsed, this, sentence] | [correctly] |  | SHIFT |
|[ROOT, parsed, sentence] | [correctly] | sentence -> this | LEFT-ARC |
|[ROOT, parsed] | [correctly] | parsed -> sentence | RIGHT-ARC |
|[ROOT, parsed, correctly] | [] |  | SHIFT |
|[ROOT, parsed] | [] | parsed -> corectly | RIGHT-ARC |
|[ROOT] | [] | ROOT -> parsed | RIGHT-ARC |

### (b) 2n, n번의 shift + n번의 arc

### (e) dev set: 88.42, test set: 89.10

### (f)

Prepositional Phrase Attachment Error
Verb Phrase Attachment Error
Modifier Attachment Error
Coordination Attachment Error

i.

- Error Type: Verb Phrase Attachment Error
- Incorrect dependency: wedding -> fearing
- Correct dependency: heading -> fearing

ii.

- Error Type: Coordination Attachment Error
- Incorrect dependency: makes -> rescue
- Correct dependency: rush -> rescue

iii.

- Error Type: Prepositional Phrase Attachment Error
- Incorrect dependency: named -> Midland
- Correct dependency: guy -> Midland

iv.

- Error Type: Modifier Attachment Error
- Incorrect dependency: elements -> most
- Correct dependency: crucial -> most
