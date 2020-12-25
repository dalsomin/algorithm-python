'''
문자열과 내장함수
'''
msg = "It-is-Time"

print(msg.upper())
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find('T')) # 인덱스 출력된다.
print(tmp.count('T'))
print("----------------------")

print(msg)
print(msg[:2]) #0번부터 1번까지 슬라이스 한다.
name = '0123456789'
print(name[:6])#012345
print(name[2:6])#2345
print(name[4:6])#45
print(len(name))
for i in range(len(msg)):
    print(msg[i], end='  ')
print()
print("-------")
for x in msg:
    print(x, end=' ')
print()
for x in msg:
    if x.isupper():
        print("대문자:",x)
    else:
        print("소문자:",x)
print("---------")
#아스키 넘버 - 대문자 
tmp='AZ'
for x in tmp:
    print(ord(x))

# 아스키 넘버 - 소문자
tmp2='az'
for x in tmp2:
    print(ord(x))

tmp3=65
for i in range(tmp3, 130):
    print(chr(i), end=' ')

print("알파벳 대문자는 %s 부터, %s까지 소문자는 %s부터 %s까지"  % (chr(65), chr(90), chr(97), chr(122)))

print()

for i in range(65, 123):
    if chr(i).isalpha:
        print(chr(i), ":", i)

