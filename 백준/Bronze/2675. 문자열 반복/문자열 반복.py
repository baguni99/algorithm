R=int(input())

for _ in range(R):
    S=list(input())
    for i in range(2,len(S)) :
        print((S[i]*int(S[0])),end='')
    print()