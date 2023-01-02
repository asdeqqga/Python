"""
날짜 : 2023/01/02
이름 : 라성준
내용 : 백준 문제 1단계 10번
"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b)%c)
print(((a % c) * (b % c)) % c)