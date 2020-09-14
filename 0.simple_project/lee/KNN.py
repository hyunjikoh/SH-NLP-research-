from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import numpy as np


iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], test_size = 0.3, random_state=1)
kfold = KFold(n_splits=3, shuffle=True, random_state=0)

best_k = 0
max = 0

for k in range(3,20):
    knn = KNeighborsClassifier(k)
    scores = cross_val_score(knn, X_train, y_train, cv = kfold, scoring='accuracy')
    print("%d일때 정확도 : " %k + str(scores))
    if max < np.mean(scores):
        max = np.mean(scores)
        best_k = k


knn = KNeighborsClassifier(n_neighbors=best_k) #데이터 셋으로부터 모델 만들기
knn.fit(X_train, y_train)

print("k가 %d일때 가장 정확한 결과값이 나왔으며, 테스트 세트의 정확도는 {:.2f}입니다. ".format(knn.score(X_test, y_test)) %best_k)