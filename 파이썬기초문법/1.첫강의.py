'''
변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 대소문자 구분
3) 문자나 _로 시작한다.
4) 특수문자 사용불가
5) 예약된 특수 문자를 사용하면 안된다.
'''
a = 1
A = 2
_a = 3
print(a, A, _a)

b, c, d = 4, 6, 8

print(b, c, d)
# 변수 값 바꿔 넣기~
b, c, d = a, A, _a

print(b, c, d)

#8바이트 = 64bit
#1바이트 = 8bit

# 8바이트가 넘어가면 자동으로 자른다.

f = 12.123456789123456789123456789
print(f)
#12.123456789123457 결과값
print(type(f))

name = "dalsomin"
print(name)
print(type(name))

a,b,c = 3 ,6,9
print(a,b,c, sep="-----")
print(a,b,c, sep="--\n")
print(a,b,c,)

# 줄바꿈 없애준다
print(b, end=' ')
print(b, end=' ')
print(b, end=' ')
print(b, end=' ')
