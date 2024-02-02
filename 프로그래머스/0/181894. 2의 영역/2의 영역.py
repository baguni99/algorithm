def solution(arr):
    if 2 not in arr:
        return[-1]
    start_index=arr.index(2)
    end_index=arr[::-1].index(2)
    end_index=len(arr)-1-end_index
    return arr[start_index:end_index+1]