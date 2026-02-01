def find_length(nums, k):
    left = cur = 0
    res = -1

    for right in range(len(nums)):
        cur += nums[right]

        while cur > k:
            cur -= nums[left]
            left += 1

        res = max(res, right - left + 1)

    return res