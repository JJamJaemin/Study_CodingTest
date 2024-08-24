import sys

n,k = map(int,sys.stdin.readline().split())
height_list = list(map(int,sys.stdin.readline().split()))
dis = [] #각 인접한 유치원 생들의 키 차이
answer = 0

for i in range(n-1):
    dis.append(height_list[i+1] - height_list[i]) #인접한 키 차이를 추가
dis = sorted(dis, reverse=True) #큰 순별로 정렬

answer = sum(dis[k-1:]) 

print(answer)