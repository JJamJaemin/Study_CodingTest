while(True):
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        break
    else:
        if B % A == 0 and B > A:
            print("factor")
        elif A > B and A % B == 0:
            print("multiple")

        else:
            print("neither")