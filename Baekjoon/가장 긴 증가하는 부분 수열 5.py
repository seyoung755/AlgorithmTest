import sys 
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = []
result.append(-sys.maxsize)
answer = []
for num in arr:
    # print(result)
    left, right = 0, len(result)-1

    while left < right:
        mid = (left + right) // 2
        # print(mid)
        if result[mid] < num:
            left = mid+1
        else:
            right = mid-1
    
    if left >= right:
        if result[left] < num:
            if left < len(result)-1:
                result[left+1] = num
                answer.append(left+1)
            else:
                result.append(num)
                answer.append(len(result)-1)
        else:
            result[left] = num
            answer.append(left)
    
# print(result)
length = len(result)-1
print(length)

# LIS = []

# for idx in range(len(answer)-1, -1, -1):
#     if answer[idx] == length:
#         LIS.append(arr[idx])
#         length -= 1



# # print(answer)
# for num in LIS[::-1]:
#     print(num, end=' ')
# print(" ".join(list(map(str, answer[1:]))))
