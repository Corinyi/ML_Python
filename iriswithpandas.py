import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')

# 데이터 칼럼 추출하기

csv_data = csv[["sepal.length","sepal.width","petal.length","petal.width"]]
csv_label = csv[["variety"]]

# header column 0(컬럼명) 제거
# del csv[0]

print(csv_data)
# 훈련데이터와 테스트데이터 분리

X_train, X_test, y_train, y_test = train_test_split(csv_data, csv_label)

clf = svm.SVC()
# 학습모델
clf.fit(X_train, y_train)

# 테스트
predict_label = clf.predict(X_test)

# 정확도
ac_score = metrics.accuracy_score(y_test, predict_label)

print("정확도 : ", ac_score )