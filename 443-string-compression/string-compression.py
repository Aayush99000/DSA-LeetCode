class Solution:
    def compress(self, chars):
        w = 0  # write pointer
        i = 0  # read pointer

        while i < len(chars):
            current_char = chars[i]
            count = 0

            # Step 1: Count the group
            while i < len(chars) and chars[i] == current_char:
                i += 1
                count += 1

            # Step 2: Write the character
            chars[w] = current_char
            w += 1

            # Step 3: Write count digits (only if > 1)
            if count > 1:
                for digit in str(count):
                    chars[w] = digit
                    w += 1

        return w
