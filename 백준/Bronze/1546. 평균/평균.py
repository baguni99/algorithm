n=int(input())
score_list=list(map(int,input().split()))
max_score=max(score_list)
new_max_score=[]
for score in score_list :
    new_max_score.append(score/max_score*100)
avg=sum(new_max_score)/n
print(avg) 