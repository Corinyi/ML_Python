from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

# 키와 몸무게 데이터를 읽어오기
data = pd.read_csv("bmi.csv")

# 컬럼(열) 분리
label = data['label']
h = data['height'] / 200
w = data['weight'] / 100

wh = pd.concat([w,h],axis=1)

# 학습 데이터와 테스트 데이터로 나누기
data_train, data_test, label_train, label_test = train_test_split(wh,label)

clf = svm.SVC()
clf.fit(data_train, label_train)
predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
print("정확도 : ", ac_score)