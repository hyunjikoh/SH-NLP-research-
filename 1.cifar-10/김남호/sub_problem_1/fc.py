# https://www.tensorflow.org/tutorials/images/cnn?hl=ko
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.layers import Dropout
from tensorflow.keras import optimizers


def fullyConnectedCifar10():
    """
    32*32*3 이미지를 3072*1의 input 으로 변경
    """
    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

    print("original Train samples:", train_images.shape, train_labels.shape)
    print("original Test samples:", test_images.shape, test_labels.shape)

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    model = models.Sequential(name="only_fully_connected_model")
    model.add(layers.Flatten())
    model.add(layers.Dense(100, activation='relu'))
    # model.add(layers.Dense(1024, activation='relu'))
    # model.add(Dropout(0.2))
    # model.add(layers.Dense(256, activation='relu'))
    # model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    model.build((None, 3072))
    model.summary()

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, batch_size=64, epochs=30, shuffle=True)

    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Test loss: ', test_loss, 'Test accuracy: ', test_acc)


if __name__ == '__main__':
    fullyConnectedCifar10()
