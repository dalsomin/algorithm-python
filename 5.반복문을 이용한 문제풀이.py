'''
# 홀수 출력하기 
n = int(input("숫자 넣으세요:"))
for i in range(1, n+1):
    if i%2==1:
        print(i)


# 1~n까지 더하기 
n = int(input("숫자 넣으세요:"))
sum =0
for i in range(1, n+1):
    if i%2==1:
        sum=sum+i
        print(sum)
print("===",sum)
'''

# 약수 출력하기
n = int(input("숫자 넣으세요:"))
for i in range(1, n+1):
    if n%i==0:
        print(i, end=' ')
