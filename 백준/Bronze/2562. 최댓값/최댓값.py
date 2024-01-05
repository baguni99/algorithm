N=[]
for i in range(9):
    i=int(input())
    N.append(i)
print(max(N))
print(N.index(max(N))+1)
