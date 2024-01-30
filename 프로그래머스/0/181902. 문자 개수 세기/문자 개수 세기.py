def solution(my_string):
    answer = [0 for i in range(52)]
    tmp=[]
    for i in range(len(my_string)):
        if ord(my_string[i])<=90:
            tmp.append(ord(my_string[i])-65)
        else :
            tmp.append(ord(my_string[i])-71)
    for j in range(len(tmp)):
        answer[tmp[j]]=answer[tmp[j]]+1
    return answer