
def rob(nums: list[int]):
    if len(nums) < 2:
        return max(nums + [0])
    def regular_rob(l,r):
        last, now = 0, 0
        while l < r:
            last, now, l = now, max(last + nums[l], now), l+1
        return now
    return max(regular_rob(1, len(nums)), regular_rob(0, len(nums)-1))
