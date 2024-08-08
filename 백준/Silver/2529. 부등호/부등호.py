from itertools import permutations

k = int(input())
k_list = list(map(str, input().split()))
number = [0,1,2,3,4,5,6,7,8,9]

answer = []
max = ''
min = ''

for answer_list in permutations(number,k+1):
    status = True
    for j in range(k):
        if k_list[j] == '>' and not (answer_list[j] > answer_list[j+1]):
            status = False
            break
        elif k_list[j] == '<' and not (answer_list[j] < answer_list[j+1]):
            status = False
            break
    if status == True:
        answer.append(answer_list)
for i in answer[0]:
    min += str(i)
for i in answer[-1]:
    max += str(i)
print(max)
print(min)