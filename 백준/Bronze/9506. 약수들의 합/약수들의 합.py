while(1):
    n=int(input())
    if n==-1:
        break
    else :
        s=[]
        for i in range(1, n):
            if n%i==0:
                s.append(i)
        if sum(s)==n:
            print(n,'= ',end='')
            print(*s[0:],sep=' + ')
        else :
            print(n,'is NOT perfect.')
