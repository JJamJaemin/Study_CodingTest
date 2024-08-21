n,k = map(int,input().split())
table_list = list(input().rstrip())

answer = 0
for i in range(n):
  if table_list[i] == 'P': #사람일때
    for j in range(i-k,i+k+1): #사람이 있는 위치에서 -k , +k 위치까지 탐색
      if -1 < j < n: #i 가 첫번째 일때는 오류가 나므로 예외처리
        if table_list[j] == 'H': #왼쪽부터 햄버거를 찾으면
          table_list[j] = 'x' #햄버거를 없앰
          answer+=1 #먹은 인원수 증가
          break #먹었으면 바로 다음 인원 탐색

print(answer)
