N = int(input()) #포도주 잔의 갯수
A = [int(input()) for _ in range(N)] #포도주 잔 별 양
dp = [0] * N
if N == 1:
  print(A[0])
elif N == 2:
  print(A[0] + A[1])
else:
  dp[0] = A[0] #첫번재 잔만 마신경우
  dp[1] = A[0] + A[1] #첫번째 잔 + 두번째 잔 마신경우 ## 즉 세번째 잔을 마시지 않은경우
  dp[2] = max(A[0] + A[2], A[1] + A[2], dp[1]) #(1,3)(2,3)(3번째 안마신경우) 중 최대

  #dp[i-1] = i번째 와인잔을 마시지 않은 경우
  #dp[i-2] + A[i] = i번째를 마시고 i-1번째 잔을 마시지 않은 경우
  #dp[i-3] + A[i} + A[i-1] = i-2번째 잔을 마시지 않고 i-1, i 번째 잔을 먹었을 경우
  for i in range(3,N):
    dp[i] = max(dp[i-1], dp[i-2] + A[i], dp[i-3] + A[i] + A[i-1])

  print(max(dp))





