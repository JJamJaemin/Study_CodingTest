n = int(input()) #city의 갯수
city = list(map(int, input().split())) #city별 요청 금액
m = int(input()) #총예산
city.sort()
start = 0
end = city[-1]

while start <= end:
  mid = (start + end) // 2
  total = 0

  for i in city:
    total += min(i, mid)

  if total > m:
    end = mid - 1
  else:
    start = mid + 1
print(end)



