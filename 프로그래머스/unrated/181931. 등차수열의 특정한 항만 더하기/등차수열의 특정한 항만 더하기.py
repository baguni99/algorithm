def solution(a,d,included) :
    result = 0
    for i in range(len(included)):
        result += (a+d*i)*int(included[i])
    return result