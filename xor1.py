from sklearn import svm

xor_data = [
	[0,0,0],
	[0,1,1],
	[1,0,1],
	[1,1,0]
]
#학습데이터와 레이블을 분리
data = []
label = []

for row in xor_data:
	p=row[0]
	q=row[1]
	res=row[2]

	data.append([p,q])
	label.append(res)

#SVM을 알고리즘을 사용하는 머신러닝 객체를 만든다.
clf = svm.SVC()
clf.fit(data, label)


pre = clf.predict(data)
print("예측결과 :", pre)

ok = 0; total =0
for idx, answer in enumerate(label):
	p = pre[idx]
	if p == answer: ok += 1
	total += 1
print("정답률:", ok, "/", total, "=", ok/total)