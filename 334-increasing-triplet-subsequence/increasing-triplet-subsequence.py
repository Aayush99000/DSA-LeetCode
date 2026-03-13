class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')

        for n in nums:
            if n <= first:
                first = n           # new smallest first candidate
            elif n <= second:
                second = n          # new smallest second candidate (first < n)
            else:
                return True         # first < second < n → triplet found!

        return False
        