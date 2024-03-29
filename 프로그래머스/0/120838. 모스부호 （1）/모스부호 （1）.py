def solution(letter):
    answer = ''
    trans = ''
    tmp = ''
    cnt = 0
    length = len(letter)
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    for i in letter:
        cnt += 1
        if i == ' ' :
            trans += morse[tmp]
            print('cnt',cnt)
            print('length',length)
            print('tmp', tmp)
            tmp = ''
        else:
            tmp += i
        if cnt == length:
            trans += morse[tmp]
    answer = trans
    return answer