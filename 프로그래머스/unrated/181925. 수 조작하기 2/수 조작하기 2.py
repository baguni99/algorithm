def solution(numLog):
    result=[]
    prev_num = numLog[0]

    for i in range(1,len(numLog)):
        diff = numLog[i] - prev_num

        if diff == 1:
            result.append("w")
        elif diff == -1:
            result.append("s")
        elif diff == 10:
            result.append("d")
        elif diff == -10:
            result.append("a")

        prev_num=numLog[i]
    return ''.join(result)