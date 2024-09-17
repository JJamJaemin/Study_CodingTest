import itertools

n = int(input())
answer = list(itertools.permutations(list(range(1,10)),3)) #정답 가능한 것

for i in range(n):
    num, strike, ball = map(int, input().split())
    guess = list(map(int,str(num)))

    correct = []
    for k_answer in answer:
        tmp_strike, tmp_ball = 0, 0

        for tmp in range(3):
            if guess[tmp] == k_answer[tmp]:
                tmp_strike += 1
            if guess[tmp] != k_answer[tmp] and guess[tmp] in k_answer:
                tmp_ball += 1
        if tmp_strike == strike and tmp_ball == ball:
            correct.append(k_answer)
    answer = correct #정답 가능한것 업데이트

print(len(correct))




