k, n = map(int, input().split())
cable = []
for i in range(k):
    cable.append(int(input()))

cable = sorted(cable)

def find_length():
    start = 1
    end = cable[-1]
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in cable:
            tmp += i // mid
        if tmp >= n:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

print(find_length())
