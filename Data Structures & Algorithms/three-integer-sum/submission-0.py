class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            first = i + 1
            second = len(nums) - 1

            while first < second:
                current_sum = nums[i] + nums[first] + nums[second]

                if current_sum < 0:
                    first += 1

                elif current_sum > 0:
                    second -= 1

                else:
                    result.append([nums[i], nums[first], nums[second]])

                    first += 1
                    second -= 1

                    while first < second and nums[first] == nums[first - 1]:
                        first += 1

        return result