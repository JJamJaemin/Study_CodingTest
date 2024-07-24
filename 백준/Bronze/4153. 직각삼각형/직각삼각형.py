while True:
    ls = list(map(int, input().split()))
    a = sorted(ls)
    if a == [0,0,0]:
        break
    else:
        if a[-1] * a[-1] == (a[0]*a[0]) + (a[1]*a[1]):
            print("right")
        else:
            print("wrong")