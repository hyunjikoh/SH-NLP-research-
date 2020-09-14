from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()


x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)

# x_train 데이터 보기
# iris_dx = pd.DataFrame(x_train, columns=iris.feature_names)
# print(iris_dx[:5])

max =0
neighbor = 0

for k in range(1, 20):
    test_scores = []
    knn = KNeighborsClassifier(n_neighbors=k)

    # cross_val_score 함수에는 KFold의 매개변수를 제어할 수가 없으므로, 따로 KFold 객체를 만들고 매개변수를 조정한 다음에 cross_val_score의 cv 매개변수에 넣어야
    kfold = KFold(n_splits=5, shuffle=True, random_state=0)
    # x_train으로 train과 validation으로 fold 되도록
    scores = cross_val_score(knn, x_train, y_train, cv=kfold, scoring='accuracy')
    if max <= scores.mean():
        max = scores.mean()
        neighbor = k

    print("K is %d, test score's mean %f" % (k, scores.mean()))

print("Optimized K is %d" %(neighbor))


knn = KNeighborsClassifier(n_neighbors=neighbor)
#?? train으로 넣는 것이 맞는가?
knn.fit(x_train, y_train)
test_score = knn.score(x_test, y_test)

print("Mean of Accuracy (test case) is %f" % (test_score.mean()))
