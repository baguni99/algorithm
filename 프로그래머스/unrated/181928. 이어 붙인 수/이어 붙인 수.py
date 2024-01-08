def solution(num_list):
    answer = 0
    odd_list=""
    even_list=""
    for i in range(len(num_list)):
        if num_list[i]%2==1 :
         odd_list+=str(num_list[i])
        else :
         even_list+=str(num_list[i])
    answer=int(odd_list)+int(even_list)
    return answer