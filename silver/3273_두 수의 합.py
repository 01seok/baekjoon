N = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()     # 숫자 리스트 오름차순 정렬

cnt = 0         # 몇 쌍이 있는지 확인할 변수 cnt
left = 0        # 왼쪽
right = len(nums) - 1   # 오른쪽

while left < right: # 왼쪽이 오른쪽보다 왼쪽에 있을 때(더 작을 때)
    current_sum = nums[left] + nums[right]  # 현재 숫자는 nums 배열 좌측 숫자 + 우측 숫자

    if current_sum == x:    # 같으면
        cnt += 1            # 1페어 증가
        left += 1           # 다음 숫자 확인 위해 왼쪽에서 오른쪽으로 한칸
        right -= 1          # 다음 숫자 확인 위해 오른쪽에서 왼쪽으로 한칸

    elif current_sum < x:   # 현재 숫자가 x보다 작다면
        left += 1           # 더 큰 숫자를 더해야하니 좌측 > 우측으로 한칸

    else:
        right -= 1

print(cnt)



# cnt = 0
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums [i] + nums[j] > x:
#             continue
#         if nums[i] + nums[j] == x:
#             cnt += 1
#
# print(cnt)

