import  pandas as pd
from sklearn import svm, metrics

#XOR 연산 데이터

inputData = [
	[0,0,0],
	[0,1,1],
	[1,0,1],
	[1,1,0]
]

xor_df = pd.DataFrame(inputData)
#학습데이터와 레이블을 분리
trainingData = xor_df.loc[:,0:1]
label = xor_df.iloc[:,2]

#머신러닝 객체 만들기
clf=svm.SVC()

#데이터의 학습과 예측
clf.fit(trainingData, label)
pre = clf.predict(trainingData)

#정확도 측정(정답률)
#metrics 모듈에 accuracy_score 함수 이용하면 성공률 구할 수 있다.

accuracy = metrics.accuracy_score(label, pre)
print("정확도: ", accuracy)