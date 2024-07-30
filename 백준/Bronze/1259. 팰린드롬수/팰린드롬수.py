import sys
while True:
    N = sys.stdin.readline().strip()
    if N == '0':
        break
    if len(N) % 2 == 0: #짝수면 %2 +1 만큼 체크
        sts = True
        for i in range(len(N)//2 + 1):
            if N[i] == N[-1-i]:
                sts = True
            else:
                sts = False
                break
    else:
        sts = True
        for i in range(len(N)//2):
            if N[i] == N[-1-i]:
                sts = True
            else:
                sts = False
                break
    if sts == True:
        print("yes")

    else:
        print("no")


