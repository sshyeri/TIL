nums = [float(input()) for _ in range(int(input()))]
mul = [nums[0]]
for i in range(1, len(nums)):
    mul.append(max(nums[i], nums[i]*mul[-1]))
print("%.3f"%(max(mul)))
