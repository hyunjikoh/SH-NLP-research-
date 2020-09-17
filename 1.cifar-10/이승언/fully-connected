from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import cifar10
from tensorflow.keras import layers

# 데이터셋 생성하기(정규화)
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train = x_train / 255.0
x_test = x_test / 255.0

# 원-핫 인코딩
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# 모델 구성하기
model = Sequential()
model.add(layers.Flatten())
model.add(Dense(units=128, input_dim=32*32, activation='relu')) #units은 다음 레이어의 노드수, input_dim은 들어가는 뉴런수
model.add(Dense(units=10, activation='softmax'))


# 모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 모델 학습시키기
hist = model.fit(x_train, y_train, epochs=5, batch_size=32) #batch_size는 몇문항까지 풀고 해답이랑 비교할지


print('## training loss ##')
print(hist.history['loss'])


result = model.evaluate(x_test, y_test, batch_size=32)
print('##  loss and accuracy ##')
print(result)

