H,M=map(int,input().split())
if 45>M :
    if H==0:
        H=23
    else: H-=1
    print (H,M+15)
elif M>=45:
    print (H,M-45)