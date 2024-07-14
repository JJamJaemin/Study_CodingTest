word = input()
length = len(word)
max_length = length
list = [['None' for i in range(15)] for j in range(5)]
for j in range(length):
    list[0][j] = word[j]
for i in range(4):
    word = input()
    length = len(word)
    if length > max_length:
        max_length = length
    for j in range(length):
        list[i+1][j] = word[j]
for i in range(15):
    for j in range(5):
        if list[j][i] != 'None':
            print(list[j][i], end='')