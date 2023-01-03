"""
날짜 : 2023/01/02
이름 : 라성준
내용 : 백준 문제 1단계 2588번
"""
num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)