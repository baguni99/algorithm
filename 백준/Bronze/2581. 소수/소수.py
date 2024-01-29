M=int(input())
N=int(input())
s=[]
for i in range(M,N+1) :
    error=0
    if i > 1 :
        for num in range(2,i):
            if i % num == 0:
                error +=1
                break
        if error ==0 :
            s.append(i)
if len(s) >0 :
    print(sum(s))
    print(min(s))
else:
    print(-1)        