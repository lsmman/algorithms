# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 30초 / C++의 경우 30초 / Java의 경우 30초 / Python의 경우 30초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def getRowArray(matrix, i):
    return matrix[i]


def getColArray(matrix, i):
    return [m[i] for m in matrix]


def check_valid(arr, X):

    return 0


def solution(N, X, matrix):
    count = 0
    for i in range(N):
        count += check_valid(getRowArray(matrix, i), X)
        count += check_valid(getColArray(matrix, i), X)
    return count


if __name__ == "__main__":
    sys.stdin = open("python-programmers\활주로_건설.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        matrix = []
        N, X = map(int, input().split())
        for _ in range(N):
            matrix.append(list(map(int, input().split())))
        ans = solution(N, X, matrix)
        print("#{} {}".format(t, ans))
        break


"""
Sample Output
#1 7

#2 4

#3 11

#4 11

#5 15

#6 4

#7 4

#8 1

#9 5

#10 8
"""