N = int(input())
A = list(map(int, input().split()))

dp = [0]*N
for i in range(N):
  if i == 0:
    dp[i] = 1 #초기 값 만들 수 있는 수열은 1개 이므로 길이 1
  else:
    tmp = []
    for j in range(i):
      if A[j] > A[i]: # 전 숫자들중 자신보다 큰 숫자가 있는지 조건
        tmp.append(dp[j]+1) #있으면 자기 자신을 포함한 수열 길이로 tmp에 저장
      else:
        tmp.append(1) #없다면 자기 자신만 포함하는 1 저장
    dp[i] = max(tmp) #가장 큰 길이를 선택
print(max(dp))
