# 파이썬을 이용한 머신러닝과 딥러닝 기초다지기 


### Base of Machine Learning and Deep Learning Using Python 


##### 성균관대학교 하계 도전학기(2020)


![screensh](./images/pythonmldl.jpg)

### 1주차 
1. 인공지능과 머신러닝
    - 기존의 알고리즘
        - 외부 데이터 -> 기존 알고리즘 -> 결과값
        - 합리주의 관점, 알고리즘에 정립된 정보(논증 체계)가 들어감, 데이터가 외부에서 입력되면, 정보(논증 체계)를 거쳐 결과값 도출함.
    - 머신러닝 알고리즘
        - raw 데이터 + (결과값) -> 머신러닝 알고리즘 -> 알고리즘
        - raw 데이터와 결과값(안들어가는 경우도 있음)이 들어감, 수많은 케이스에 대한 경험을 얻고, 정보(논증 체계)를 구축함. 즉 데이터가 들어가서 알고리즘이 도출됨.


2. 머신러닝 알고리즘

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
    - scipy.sparse 함수
    scipy에서 scikit-learn 알고리즘을 구현할 때, 많이 사용하는 모듈
    - 희소행렬(Sparse matrix): 0을 많이 포함한 2차원 배열
    - sparse.csr_matrix()
    0이 아닌 원소만 저장하는 method, 순서쌍으로 행렬의 값을 나타내줌
    - COO 포멧(Coordinate)
    
11. matplotlib
    - 과학 계산용 그래프 라이브러리
    선그래프, 히스토그램, 산점도 등 지원
    - pyplot 모듈 이용
    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    plt.plot(x,y, linestyle="--", label="이름")
    plt.tytle("그래프 이름")
    plt.xlabel("x축 이름")
    plt.legend() #범례
    plt.show() #그래프 출력
    ```


12. scikit-learn의 데이터셋 소개


### 3주차 

13. train데이터와 test 데이터 분리하기
    훈련데이터와 평가 데이터가 같으면 안됨.
    보통 8:2로 훈련데이터와 평가데이터를 나눔.
    그냥 바로 테스트로 스필릿하면 안됨
    3개의 붓꽃 클래스를 잘 섞어서 데이터 조함해야함.
    -> 난수 생성기의 필요성
    - dataset 설정
        load_iris 함수가 리턴하는 객체는 Bunch 클래스 객체
        Bunch 클래스 객체는 파이썬의 Dict과 유사한 객체
        key, value로 구성됨
    - train_test_split()
        훈련데이터와 테스트 데이터를 나눔
        sklearn.model_selection 에 있음
14. 붓꽃 품종 분류기 1
15. 붓꽃 품종 분류기 2
    - scikit-learn에서는 항상 2차원 배열
    - 정확도 판별
    numpy 에 있는 mean  값을 이용해서 정확도 판별 가능
    또는 knn 의 score method를 이용해도 가능

16. 붓꽃 품종 분류기 3

### 4주차

17. 붓꽃 품종 분류기 4
18. SVM 알고리즘 1
19. SVM 알고리즘 2
