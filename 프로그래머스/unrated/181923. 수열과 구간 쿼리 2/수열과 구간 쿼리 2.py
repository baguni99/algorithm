def solution(arr, queries):
    result = []

    for query in queries:
        s, e, k = query
        sub_arr = arr[s:e+1]  # 시작과 끝 지점을 포함한 부분 배열 추출
        sub_arr.sort()  # 부분 배열을 오름차순으로 정렬

        # k보다 크면서 가장 작은 값을 찾기
        answer = -1
        for num in sub_arr:
            if num > k:
                answer = num
                break

        result.append(answer)

    return result