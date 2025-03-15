nums = set()

for _ in range(10):
    num = int(input())
    
    nums.add(num % 42)
    
print(len(nums))