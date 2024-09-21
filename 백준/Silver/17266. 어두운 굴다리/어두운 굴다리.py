n = int(input()) #굴다리 길이
m = int(input()) #가로등 개수
locate = list(map(int, input().split())) #가로등 위치

#가로등 높이
height = 0

height = max(height, locate[0])
for i in range(1,m):
    if (locate[i]-locate[i-1]) % 2 == 0:
        height = max(height, (locate[i] - locate[i-1])//2)
    else:
        height = max(height, (locate[i] - locate[i-1])//2+1)
height = max(height, n - locate[-1])

print(height)
