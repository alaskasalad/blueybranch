def find_best_subarray(nums, k):
    cur =  0
    for i in range(k):
        cur += nums[i]

# 3, -1, 4, 12, -8, 5, 6
# 18
    ans = cur
    for i in range(k, len(nums)):
        cur += nums[i] - nums[i - k]

        ans = max(ans, cur)
    return ans