'''
함수만들기

def add(a,b):
    print(a+b)
add(1, 4)

'''

def add(a,b):
    return a+b

print(add(2, 5))


def add2(a,b):
    c = a+b
    d= a-b
    return c,d

print(add2(8,5))



# 소수인지 아닌지를 알려주는 함수를 만들어보자
# 참거짓을 리턴하는 함수
# 2부터 x 자기자신 전까지의 수까지 돌꺼다
# 소수는 1과 자기자신빼고는 나누어떨어지는 수가 없어야한다.


def isPrime(x):
    for i in range(2, x):
        if x%i ==0: # 이게 참이라면 i는 x의약수가 된다.
            return False
        return True
    
print(isPrime(13))
sosu = [12,13,7,9,19,31,30]
for x in sosu:
    if isPrime(x):
        print(x, end=' ')
