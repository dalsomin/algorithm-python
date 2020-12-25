'''
리스트와 내장함수(2)
'''

a = [23, 12, 36, 53, 19]
print(a[:3])
a.sort()
print(a)
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()
print("-----")
for x in enumerate(a):
    print(x)

# 튜플
b=(1,2,3,4,5)
print(b[0])
# 튜플은 이렇게 값을 변경하는것이 절대 불가능하다. b[0]=7 (x)
print(b)
#enumerate
for x in enumerate(a):
    print(x[0], x[1])

for index, value in enumerate(a):
    print(index, value)

# all
if all(30>x for x in a): # for x in a 가 하나하나 돌면서 모두 참이어야 참이다.
    print("yes")
else:
    print("no")

print(a)
#any
if any(10>x for x in a): # 하나하나 돌면서 하나라도 참이면 참이다.
    print("yes")
else:
    print("no")
