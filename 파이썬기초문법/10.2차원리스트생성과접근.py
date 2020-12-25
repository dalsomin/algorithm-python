'''
2차원 리스트 생성과 접근
'''
#1차원리스트 생성
a = [1]*3
print (a)

# 2차원리스트 생성법

b = [[0]*3 for _ in range(5)]
print(b)
b[0][1] = 5
b[2][2]=7
print(b)
print("==========")
for x in b:
    print(x)

for x in b:
    for y in x: # 1차원리스트의 하나하나의 값을 뺴는거니까 대괄호가 사라짐
        print(y, end=' ')
    print()
