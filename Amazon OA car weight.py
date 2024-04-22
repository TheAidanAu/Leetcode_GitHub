def min_number_of_drivers(nums, k):
    if len(nums) < 2:
        return 0

    skips = 0
    l, r = 0, 1

    while r < len(nums):
        if nums[l] + nums[r] > k:
            skips += 1
            if nums[l] > nums[r]:
                l = r
        else:
            l = r
        r+=1
