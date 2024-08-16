N,M = map(int,input().split()) #N:입국심사대수 M : 인원수
T = [int(input()) for i in range(N)] #입국 심사대 소요시간

start = min(T)
end = max(T) * M
answer = end #answer의 초기값은 가장 작은 시간을 구하는 것으므로 큰값으로 초기화 해놓는다.
while start <= end:
  mid = (start + end) // 2 #중간 시간
  can_people = 0 #가능한 수용인원
  for i in T:
    can_people += mid//i # 중간시간을 입국 심사대으 소요시간으로 나눠 가능한 각 심사대의 인원을 더함

  if can_people >= M:
    end = mid - 1
    answer = min(answer, mid) #현재 중간 시간이 더 작은가, 지금까지 나온 결과 값이 작은지 저장하기 위해
  else: #현재 중간 값으로 모든 인원을 수용하지 못하면 중간값을 늘린다.
    start = mid + 1
print(answer)







