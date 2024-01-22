number=int(input()) #색종이의 수
canvas=[[0]*101 for i in range(100)]
for _ in range(number):
    left,bottom=map(int,input().split())

    for i in range(10):
        for j in range(10):
            canvas[left+i][bottom+j]=1
black_paper=0
for i in canvas:
    black_paper+=sum(i)
print(black_paper)