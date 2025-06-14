nums = [int(input()) for _ in range(5)]

avg = sum(nums) // 5

nums.sort()
median = nums[2]

print(avg)
print(median)