from sklearn import svm, metrics
import random, re

#붓꽃 파일 읽어들이기
csv = []

with open('iris.csv','r',encoding='utf-8') as fp:
    #한 줄씩 읽어오기
    for line in fp:
        line = line.strip() #줄바꿈 제거
        cols = line.split(',') # 쉼표로 열 구분
        # 문자열 데이터를 숫자로 가져오기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$',n) else n
        cols = list(map(fn.cols))
        csv.append(cols)

    
# header column 0(컬럼명) 제거
del csv[0]

#데이터 섞어주기
random.shuffle(csv)

# 학습데이터와 테스트 데이터를 분할하기
total_len = len(csv)
train_len = int(total_len*2/3)

train_data = []
train_label = []