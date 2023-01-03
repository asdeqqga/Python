"""
날짜 : 2023/01/02
이름 : 라성준
내용 : 백준 문제 1단계 3003번
"""

a = [1, 1, 2, 2, 2, 8]

b = list(map(int, input().split()))

for i in range(6):
    print(a[i]-b[i], end=' ')