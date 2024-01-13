def solution(a,b,c,d):
    dice=[a,b,c,d] #주사위의 숫자들을 리스트에 저장
    abcd=dict() #각 숫자의 등장 횟수를 저장할 딕셔너리

    for num in dice: #주사위의 숫자들 하나씩 확인
        if num not in abcd: #해당숫자가 abcd라는 딕셔너리에 없다면 새로 추가
            abcd[num]=1
        else:
            abcd[num]+=1 #있다면 등장횟수 1 추가

    abcd=sorted(abcd,key=lambda x:abcd[x]) #딕셔너리의 키를 등장횟수에 따라 정렬

    if len(abcd)==1:
        return 1111*a
    elif len(abcd)==2:
        if dice.count(abcd[0])in[1,3]:
            return(10*abcd[1]+abcd[0])**2
        else:
            return (abcd[0]+abcd[1])*abs(abcd[0]-abcd[1])
    elif len(abcd)==3:
        return abcd[0]*abcd[1]
    
    return min(dice)