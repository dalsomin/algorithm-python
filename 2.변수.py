'''
변수 입력과 연산자
a = input("숫자를 입력하세요:")
print(a)


a,b = input("숫자를 입력하세요:").split()
a = int(a)
b = int(b)
print(a+b)

c, d = map(int, input("숫자를 입력하세요:").split())
print(c+d)

print(c-d)
print(c/d)  # 계산
print(c//d) # 몫
print(c%d) # 나머지
print(c**d) # 승

'''

a = 4.3
b = 5

c = a+b

print(c, type(c))
