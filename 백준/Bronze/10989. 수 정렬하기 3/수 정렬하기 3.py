import sys
ls = [0] * 10001
n = int(input())
for i in range(n):
    a = int(sys.stdin.readline())
    ls[a-1] += 1

for j in range(10001):
    if ls[j] != 0 :
        while True:
            if ls[j] == 0:
                break
            else:
                ls[j] -= 1
                print(j+1)




