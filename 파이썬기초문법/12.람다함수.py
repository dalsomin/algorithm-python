'''
람다함수만들기
'''
def plus_one(x):
    return x+1

print(plus_one(1))

# 람다함수는 변수에다가 할당을 해줘야한다. 
plus_two=lambda x: x+2
print(plus_two(1))

#람다함수는 내장함수의 인자로 쓸때 편리하다.

a = [1,2,3]
b = map(plus_two, a)
print(b)
b = list(b)
print(b)
#print(list(map(plus_one, a)))
#map(int, input())
#내장함수명int , 자료 : 자료들을 int화 시켜라...
# 즉, map함수input으로 받은애들을 돌면서 int로 바꿔라 라는 뜻

k = [5,6,7]
#print(list(map(plus_one, a)))을 람다로 써보자 
print(list(map(lambda x: x+2, k)))
#k리스트에 있는 자료가 lambda함수작업을 하나하나 수행하게 된다.

#sort함수 안에 key로 람타식을 쓴다.
#map처럼 map안에 key넣듯
