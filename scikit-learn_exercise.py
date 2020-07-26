import numpy as np
from sklearn.datasets import load_iris
irisData = load_iris()

from sklearn.model_selection import train_test_split

# scikit-learn 에서 데티터는 대문자 X로 표시하고 레이블은 소문자 y로 표현함

X_train, X_test, y_train, y_test = train_test_split(irisData['data'],irisData['target'], random_state=0)

#train_test_split() return 타입은 numpy 배열

# KNN(L Nearest Neighbors) : 사용하기 쉬운 분류 알고리즘; 분류기
# k는 가장까까운 이웃 하나가 아니라, 훈련 데이터에서 새로운 데이터에 가장 가까운 k개의 이웃을 찾음
# KNN을 사용하기 위해서는 neighbors 모듈에서 KNeighborsClassifier()함수 중 중요한 매개변수는
# n_neighbors 이웃의 개수를 지정하는 매개변수

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

# 훈련 데이터 셋을 가지고 모델을 만들려면 fit method를 사용
# fit method의 리턴 값은 knn 객체를 리턴함
knn.fit(X_train,y_train)

# 채집한 붓꽃을 Numpy 배열로 새로운 데이터로 가정함.
#knn predict 모듈을 이용하여 사용값을 예측할 수 있다.

X_newData = np.array([[5.1,2.9,1,0.3]])
prediction = knn.predict(X_newData)
print("예측 : {}".format(prediction))
print("예측 품종 : {}".format(irisData['target_names'][prediction]))

y_predict = knn.predict(X_test)
print("정확도 : {:.2f}".format(np.mean(y_predict==y_test)))
print("정확도 : {:.2f}".format(knn.score(X_test,y_test)))