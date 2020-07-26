from sklearn import svm

xor_data = [
	[0,0,0],
	[0,1,1],
	[1,0,1],
	[1,1,0]
]
#학습데이터와 레이블을 분리
training_data = []
label = []

for row in xor_data:
	p=row[0]
	q=row[1]
	res=row[2]

	training_data.append([p,q])
	label.append(res)
#SVM(분류, 회귀)을 알고리즘을 사용하는 머신러닝 객체를 만든다.
clf = svm.SVC()

#fit() method : 학습기계에 데이터를 학습시킴
clf.fit(training_data, label)

#predict() method : 학습데이터를 이용하여 예측한다.
pre = clf.predict(training_data)
print("예측결과 :", pre)

ok = 0; total =0
for idx, answer in enumerate(label): #enumerate 여러 변수 나열
	p = pre[idx]
	if p == answer :
		ok += 1
	total += 1
print("정확도:", ok, "/", total, "=", ok/total)