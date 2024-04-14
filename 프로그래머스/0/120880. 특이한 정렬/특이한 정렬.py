def solution(numlist, n):
    answer = []
    ls = []
    pair_ls = []
    length = len(numlist)
    tmp = 0
    for i in numlist:
        tmp = abs(n - i)
        ls.append(tmp)
    for pair in zip(numlist, ls):
        pair_ls.append(pair)
        print(pair_ls)
    pair_ls.sort(key=lambda x: (x[1], -x[0]))
    print(pair_ls)
    for a in pair_ls:
        answer.append(a[0])

    return answer