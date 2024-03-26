def solution(num, k):
    answer = 0
    st = str(num)
    answer = st.find(str(k))
    if answer != -1:
        answer += 1
    return answer