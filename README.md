# 파이썬을 이용한 머신러닝과 딥러닝 기초다지기 


### Base of Machine Learning and Deep Learning Using Python 


##### 성균관대학교 하계 도전학기(2020)


![screensh](./images/pythonmldl.jpg)

### 1주차 
<details>
<summary>1. 인공지능과 머신러닝</summary>  

#### 머신러닝의 개요   

- 기존의 알고리즘
    - 외부 데이터 -> 기존 알고리즘 -> 결과값
    - 합리주의 관점, 알고리즘에 정립된 정보(논증 체계)가 들어감, 데이터가 외부에서 입력되면, 정보(논증 체계)를 거쳐 결과값 도출함.
- 머신러닝 알고리즘
    - raw 데이터 + (결과값) -> 머신러닝 알고리즘 -> 알고리즘
    - raw 데이터와 결과값(안들어가는 경우도 있음)이 들어감, 수많은 케이스에 대한 경험을 얻고, 정보(논증 체계)를 구축함. 즉 데이터가 들어가서 알고리즘이 도출됨.
</details>

<details>
<summary>2. 머신러닝 알고리즘</summary>  

#### 머신러닝 알고리즘 분류 

1. 지도(교사)학습(Supervised Learning)
    - 학습 데이터마다 레이블(결과값)을 가지고 있음
        - 가장 기본적 형태의 머신러닝
2. 비지도 학습(Unsupervised Learning)
    - 학습 데이터에 레이블이 없음
        - 이미지에서 사물의 입력이 계속되면 사물의 특징을 도출하는 알고리즘(Clustering; 군집화, 비슷한 데이터끼리 묶기)
        - 현실의 학습과 비슷
3. 준지도 학습(Semi-Supervised Learning)
    - 학습 데이터에 일부의 레이블이 있음
4. 강화학습
    - 결과가 시간 간격을 두고 주어딤
    - 바둑이나 체스에서 Agent(바둑기사)는 State(형국)을 파악해서 Action(한 수 한 수 두는 것)을 취하고 그에 따른 Reward(action에 대한 결과)가 시간을 두고 발현되어, 최종 결과(Final Outcome)는 나중에 나옴.
</details>

3. 머신러닝의 예
4. 머신러닝의 구성요소
5. Scikit-learn 소개
6. XOR 연산 학습 1

### 2주차 

    7. XOR 연산 학습 2
        - enumerate()
        인덱스와 내용을 한번에 넘겨줌. 
    8. XOR 연산 학습 3
        - dataframe
        column 과 row 강 있고,  iloc를 이용해서 정렬 가능(ix라고 가르치지는데, 최근 pandas에서 사라짐)
        이 예제에서는 0, 1 Column이 학습데이터가 되고, 2 가 label이 됨
    9. scipy 1
        - sparse 모듈
        scipy에서 중요한 모듈
        희소행렬을(0을 많이 포함한 2차웒 행렬)

        - ones 모듈
        ones(10) 1로 10개를 채우는 함수
        사용 예
        1. numpy.ones(7)
        2. numpy.zeros(8)
        3. numpy.ones((2,3))

        - eye 모듈
        numpy에서 특수행렬을 만드는 함수
        eye(N, M= , K= , dtype) 2차원 배열을 항등 및 대각 행렬을 만들 수 있다.
        N= 행의 수, M= 열의 수,  K= 대각의 초기 위치

        - diag() 함수
        정방행렬에서 대각 요소만 추출해서 벡터를 만듬
        벡터요소를 대각요소로 하는 정방행렬을 만들기도 함
        diag(v, k=) k는 시작 위치
        np.diag(np.diag(x))

    10. scipy 2
    11. matplotlib
    12. scikit-learn의 데이터셋 소

### 3주차 

    13. train데이터와 test 데이터 분리하기
    14. 붓꽃 품종 분류기 1
    15. 붓꽃 품종 분류기 2
    16. 붓꽃 품종 분류기 3

### 4주차

    17. 붓꽃 품종 분류기 4
    18. SVM 알고리즘 1
    19. SVM 알고리즘 2
