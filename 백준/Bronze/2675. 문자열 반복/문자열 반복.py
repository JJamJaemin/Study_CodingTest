T = int(input())
for i in range(T):
    r,s = input().split()
    answer = ""
    r = int(r)
    for j in s:
        answer = answer + (j*r)
    print(answer)