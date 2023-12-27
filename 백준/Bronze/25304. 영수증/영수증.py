X=int(input())
# 영수증
N=int(input())
# 물건의 종류의 수
sum = 0
for i in range(N):
    a,b=map(int,input().split())
    # a: 물건 가격 b:갯수
    sum += a*b
if sum==X :
        print('Yes')
else :
        print ('No')