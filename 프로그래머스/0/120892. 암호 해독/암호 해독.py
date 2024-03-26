def solution(cipher, code):
    answer = ''
    length = len(cipher)
    answer = cipher[code-1:length:code]
    return answer