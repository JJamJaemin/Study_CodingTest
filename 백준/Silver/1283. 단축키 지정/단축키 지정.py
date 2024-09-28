n = int(input())
hotkey = []
answer = []

for i in range(n):
    word = input()
    words = word.split()
    setting = False
    for j in range(len(words)):
        first_char = words[j][0]
        if first_char.upper() not in hotkey:
            hotkey.append(first_char.upper())
            words[j] = '[' + first_char + ']' + words[j][1:]
            answer.append(' '.join(words))
            setting = True
            break

    if not setting:
        for char in word:
            if char.upper() not in hotkey and char != ' ':
                hotkey.append(char.upper())
                tmp = '[' + char + ']'
                index = word.index(char)
                answer.append(word[:index] + tmp + word[index + 1:])
                setting = True
                break
    if not setting:
        answer.append(word)

for i in answer:
    print(i)

