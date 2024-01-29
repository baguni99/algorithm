n=int(input()) #상단부에 숫자 입력 받고
numbers=map(int,input().split()) #그 숫자 N을 하나의 문자열로 입력 받는다. 
s=0 #소수 : 1과 자기 자신으로 나눌 때만 나누어 떨어지는 수. 
for num in numbers:
    error=0
    if num>1 :
        for i in range(2,num): 
            if num%i == 0:
                error +=1
        if error ==0 :  #error가 0이면 소수임
            s +=1
print(s)
