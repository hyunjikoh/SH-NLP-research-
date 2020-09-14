from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import numpy as np

"""
(1) train set을 5개의 fold (fold1, fold2, fold3, fold4, fold5) 로 나눕니다.

(2) 1번째 시도에서는 fold1+fold2+fold3+fold4로 모델을 만들고, fold5로 test 하여 accuracy를 냅니다.

(3) 2번째 시도에서는 fold1+fold2+fold3+fold5 로 모델을 만들고, fold4로 test하여 accuracy를 냅니다.

... 5개의 fold 하에서는 모두 5번의 시도끝에 5개의 accuracy를 구하고, 그것의 평균을 냅니다.

-> cross-validation 에 따른 accuracy 를 냅니다.

위와 같은 방법을 통해 K를 바꿔가면서 accuracy를 내고, accuracy가 가장 좋은 K를 선택하여, test set를 넣어 정확도를 계산한다.
"""

def getAccuracy(neighbors, x_train, y_train):
    means = []
    kf = KFold(n_splits=5, shuffle=True)
    for train_index, test_index in kf.split(x_train):
        classifier = KNeighborsClassifier(n_neighbors = neighbors)
        kf_x_train, kf_x_valid = x_train[train_index], x_train[test_index]
        kf_y_train, kf_y_valid = y_train[train_index], y_train[test_index]
        classifier.fit(kf_x_train, kf_y_train)
        prediction = classifier.predict(kf_x_valid)
        curmean = np.mean(prediction == kf_y_valid)
        means.append(curmean)
    return np.mean(means)

iris = load_iris()

bestAcc = 0.0
bestk = 0
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=1)
for k in range(1, 30):  #neighbor
    acc = getAccuracy(k, x_train, y_train)
    
    cls = KNeighborsClassifier(k)
    cls.fit(x_train, y_train)
    predict = cls.predict(x_test)
    accWithTest = np.mean(predict == y_test)
    print('k:{}'.format(k), 'model accuracy:{:.1%}, '.format(acc), 'test accuracy :{:.1%}'.format(accWithTest))
    if acc > bestAcc:
         bestAcc = acc
         bestk = k
print('best k :', bestk, 'best accuracy : {:.1%}'.format(bestAcc))
