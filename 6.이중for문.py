''''
중첩 반복문(2중 for문)

# 구구단
for i in range(1,10):
    for j in range(2,10):
        print(j,"x",i,"=",i*j,end='   ')
    print()

# 별찍기

for i in range(0, 5):
    for j in range(0,5):
        if i-j>=0:
            #print('(%d, %d)' % (i,j), end=' ')
            print('*', end=' ')
        else :
            print(' ', end=' ')
    print()
'''

for i in range(5):
    for j in range(5-i):
        print('*', end=' ')
    print()
