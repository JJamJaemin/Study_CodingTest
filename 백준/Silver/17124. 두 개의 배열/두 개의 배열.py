t = int(input())

for i in range(t):
    C = []
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    answer = 0

    for target in A:
        start = 0
        end = m-1
        while start < end:
            mid = (start + end) // 2
            if B[mid] < target:
                start = mid + 1
            else:
                end = mid

        if start == 0:
            tmp_answer = B[start]
        else:
            if start > 0 and abs(B[start-1] - target) <= abs(B[start] - target):
                tmp_answer = B[start-1]
            else:
                tmp_answer = B[start]
        answer += tmp_answer
    print(answer)


