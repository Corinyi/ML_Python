import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x= np.arange(0,6,0.1)

y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기고 나타내기

plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle="--", label="cos")

plt.title("sin and cos graph plotting")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
