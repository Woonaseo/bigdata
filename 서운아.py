# int input split for range print
# 입력 -> 5 R R R U D D
#출력 -> 3 4

n = int(input())
x,y = 1,1
plans = input().split()

moveTypes = ['L','R','U,','D']

for i in plans:
    if i == 'R':
        y+=1
    if i == 'L':
        y-=1
    if i == 'U':
        x += 1
    if i == 'D':
        x -= 1
print(x,y)

