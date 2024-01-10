N,M=map(int,input().split())
arr = [ i for i in range(1,N+1)]
# arr이라는 list에 1부터 N까지의 숫자를 넣는다.
for i in range(M):
    i,j=map(int,input().split())
    # M번 동안 for loop를 돌면서 i와 j를 입력 받음
    i-=1
    j-=1
    # i와 j를 0부터 시작하는 인덱스로 변환
    arr[i], arr[j] = arr[j], arr[i]

    # i번째 원소와j번째 원소를 교환
    # 오른쪽 항에 왼쪽 항의 값을 할당함으로써 두 변수의 값이 교환 됨.
print(*arr)
# 리스트 arr의 각 원소를 공백으로 구분하여 출력하는 방식

