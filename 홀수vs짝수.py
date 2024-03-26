# 풀이1
def solution(num_list):
    a = sum(num_list[0:len(num_list):2])
    b = sum(num_list[1:len(num_list):2])
    answer = max(a,b)
    return answer

# 풀이2
def solution(num_list):
    odd = 0
    even = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            odd += num_list[i]
        elif i % 2 == 1:
            even += num_list[i]
    if odd > even:
        answer = odd
    else:
        answer = even
    return answer