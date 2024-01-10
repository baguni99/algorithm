n=[]
# n을 list로 설정
for _ in range(10): #for문으로 0부터 9까지 반복
    a=int(input())
    b=a%42
    n.append(b) #append : 리스트 n에 b추가
s= set(n) #n에 저장괸 자료형의 중복을 제거해주기 위해 set함수 이용
print(len(s)) #len 함수 : 리스트 s의 길이 출력
