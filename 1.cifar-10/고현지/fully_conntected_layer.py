import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.regularizers import l2
from sklearn.model_selection import train_test_split


# CIFAR data (32x32 pixel = 784x1 pixel) - 50,000 : x_train (uint8) / 10,000 : x_text (uint8)
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# tensorflow array는 float32형이므로 uint8 -> float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# 정규화 (이미지 데이터가 0~255 사이 값을 가지므로 나눠서 0~1사이의 값으로 바꿈)
x_train = x_train / 255.0
x_test = x_test / 255.0

y_train = keras.utils.to_categorical(y_train, num_classes=10)
y_test = keras.utils.to_categorical(y_test, num_classes=10)

# train 데이터를 다시 train 과 validation 으로 나눔
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=0)

# 모델 구성
model = Sequential() # 하나의 입력 -> 하나의 출력
model.add(Flatten())
model.add(Dense(units=1024, activation='relu',kernel_regularizer=l2(0.01)))
model.add(Dense(units=512, activation='relu',kernel_regularizer=l2(0.01)))
model.add(Dense(units=256, activation='relu',kernel_regularizer=l2(0.01)))
model.add(Dense(units=10, activation='softmax',kernel_regularizer=l2(0.01))) # Fully Connected layer 딱 하나로 softmax 함수 사용
#,kernel_regularizer=l2(0.01)

# categorical_crossentropy : softmax가 마지막 layer일 대 사용 #adam / rmsprop / sgd
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# 모델 학습
# epochs => 학습사진을 재사용하도록  # batch_size => 한번에 처리하는 사진의 장 수
model.fit(x_train, y_train, epochs=10, batch_size=100, validation_data= (x_val, y_val))

# 테스트케이스로 모델 검증 / evaluate은 loss와 accuracy 보여주고, predict는 input에 대한 output 예측
score = model.evaluate(x_test, y_test)
print('#######################')
print('Loss: %.3f' % score[0])
print('Accuracy: %.3f' % score[1])

