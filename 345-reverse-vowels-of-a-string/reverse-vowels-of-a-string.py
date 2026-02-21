class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Define the vowels for quick lookup
        # We use a set for O(1) average time complexity
        vowels = set("aeiouAEIOU")
        
        # Convert to list to allow in-place modification
        chars = list(s)
        
        # Initialize two pointers
        left, right = 0, len(chars) - 1
        
        while left < right:
            # Move left pointer forward until it finds a vowel
            while left < right and chars[left] not in vowels:
                left += 1
            
            # Move right pointer backward until it finds a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # Swap the vowels at both pointers
            chars[left], chars[right] = chars[right], chars[left]
            
            # Increment and decrement to continue searching
            left += 1
            right -= 1
            
        # Join the list back into a string
        return "".join(chars)