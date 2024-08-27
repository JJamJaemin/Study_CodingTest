n = int(input())
vote = int(input())
vote_list = list(map(int, input().split()))

last_pic = [] # 최근 등록된 사진
picture = [0 for i in range(n)] #사진
pic_cnt = [0 for i in range(n)] #사진 추천 횟수


for i in vote_list:
    # print("pic",picture)
    # print("pic_cnt",pic_cnt)
    # print("last_pic",last_pic)
    if i in picture: #이미 등록된 사진일때 카운트 업
        index = picture.index(i)
        pic_cnt[index] += 1
    else:
        tmp = 0
        for j in range(len(picture)):
            if picture[j] == 0: #빈자리가 있을때 사진 등록
                picture[j] = i
                last_pic.append(i)
                pic_cnt[j] += 1
                break
            else:
                tmp += 1
        if tmp == len(picture):
            #추천수가 작은거 삭제
            min_cnt = min(pic_cnt)
            min_index = pic_cnt.index(min_cnt)
            del_pic = [index for index, value in enumerate(pic_cnt) if value == min_cnt]

            if len(del_pic) != 1 and min_cnt != 0: #가장 작은 추천이 2개 이상일때
                tmp2 = 0
                for t_2 in range(len(last_pic)):
                    for t in del_pic:
                        if picture[t] == last_pic[t_2]:
                            last_pic.remove(picture[t])
                            picture[t] = i
                            pic_cnt[t] = 1
                            last_pic.append(i)
                            tmp2 = 1
                            break
                    if tmp2 == 1:
                        break
            else: #추천수가 겹치지 않을때
                last_pic.remove(picture[min_index])
                picture[min_index] = i
                pic_cnt[min_index] = 1
                last_pic.append(i)



picture.sort()
for i in picture:
    if i != 0:
        print(i, end= ' ')
