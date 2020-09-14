from sklearn.datasets import load_iris
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold , train_test_split
from sklearn import metrics

iris = load_iris()


print(np.shape(iris.data))
print(np.shape(iris.target))

print(iris.data[1:10])

# TODO - Dataset Train/Test split
# Train : Test  = 7 : 3  = 105 : 45
X, X_test, y, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=2020)


# TODO - KFold Train/valid split


kf = KFold(n_splits=3)
kf.get_n_splits(X)



for train_index, valid_index in kf.split(X):
    X_train, X_valid = X[train_index], X[valid_index]
    y_train, y_valid = y[train_index], y[valid_index]

    valid_acc = []
    test_acc = []

    for i in range(1,10):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)

        #print('K :', i)
        #print('validation accuracy : {:.2f}'.format(knn.score(X_valid, y_valid)))
        #print('Test accuracy :{:.2f}'.format(knn.score(X_test,y_test)))

        valid_acc.append(knn.score(X_valid, y_valid))
        test_acc.append(knn.score(X_test,y_test))

    print('validation Max K value', valid_acc.index(max(valid_acc)) + 1, ' accuracy', max(valid_acc))
    print('test Max K value', test_acc.index(max(test_acc)) + 1, ' accuracy', max(test_acc))











