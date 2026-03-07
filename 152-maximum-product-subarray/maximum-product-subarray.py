class Solution(object):
    def maxProduct(self , nums):
    # Initialize with the first element
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            # Handle 0: it resets the product chain
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            # Store curMax before it gets updated
            tmp = curMax * n
            
            # Calculate new Max and Min
            # We compare: (n * curMax), (n * curMin), and the number itself
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            # Update the global result
            res = max(res, curMax)
            
        return res
        