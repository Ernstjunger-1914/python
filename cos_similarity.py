import numpy as np

# input으로 1차원 배열만
def dot(a, b):
    vector_size=len(a)
    result=0

    # result 변수에 누적
    for index in range(vector_size):
        # a와 b를 가져와서 곱한 값을 누적
        result+=a[index]*b[index]

    return result

def cosine_sim(a, b):
    # np.dot : 두 벡터를 내적하는 함수, np.linalg.norm : 벡터의 거리를 구하는 함수
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

def euclidean_distance(a, b):
    a=np.array(a)
    b=np.array(b)

    # a와 b 사이의 벡터를 구하고 norm 함수를 통해 원점에서 부터의 벡터의 길이를 구한 것이다.
    return np.linalg.norm(a-b)

if __name__=='__main__':
    arr0=[1, 2, 3]
    arr1=[2, 3, 4]

    result=euclidean_distance(arr0, arr1)
    # result=dot(arr0, arr1)
    print(result)