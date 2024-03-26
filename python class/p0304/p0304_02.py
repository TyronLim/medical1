# 숫자 5개를 입력받아 5개 출력하시오.
sum = 0
nums = []

for i in range(0,5):    
    nums.append(int(input('숫자를 입력하세요 >> ')))
    # nums[i] += 1
print(nums)

# for i in range(len(nums)):
#     sum += nums[i]
# print(sum)

for i in nums:
    sum += i

print(sum)
# print(nums)
