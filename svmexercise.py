# 2만명 데이터 작성(csv)
import random

def bmi_func(height, weight):
    bmi = weight/(height/100)**2
    if bmi < 18.5: return "low"
    if bmi < 25: return "ok"
    return "high"

fp =open('bmi.csv',"w",encoding="utf-8")
fp.write("height,weight,label\r\n")

# 데이터 생성
cnt = {'low' : 0,'ok' : 0,'high' : 0}

for i in range(10000):
    h = random.randint(120,200)
    w = random.randint(35,100)
    label= bmi_func(h,w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h,w,label))
fp.close()
print("ok, ",cnt)