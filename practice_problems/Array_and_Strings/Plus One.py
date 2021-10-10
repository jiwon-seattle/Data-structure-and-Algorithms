class Solution(object):
    # Time complexity O(N) Space complexity O(N)
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits