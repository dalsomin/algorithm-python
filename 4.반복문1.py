'''
반복문(for, while)


a = range(2,10)
print(list(a))

print("-----------")

# 2, 3, 4
for i in range(2,5):
    print("somina~")


# 작아지게
for i in range(10,0,-3):
    print(i)

#while문으로 반복문
j = 1
while j<=10:
    print(j)
    j=j+1

m = 1

while m<=10:
    if m%2==0:
        print(m)
    m=m+1
'''
#while문 나가기 break
i = 1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1

print("------------")
# continue
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

print("------------")
# for else : 정상적으로 for문이 종료됐을때 else수
for i in range(1,11):
    if i%2==0:
        continue
    print(i)
else:
    print(11)
