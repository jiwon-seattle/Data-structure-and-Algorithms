class Solution(object):
    # Time complexity O(n) Space complexity O(n)
    def trap(self, height):
        if len(height) == 0:
            return 0

        left = 0
        right = len(height)-1
        leftMax = rightMax = 0

        ans = 0

        while left < right:
            if height[left] > leftMax:
                leftMax = height[left]
            if height[right] > rightMax:
                rightMax = height[right]
            if height[left] < height[right]:
                ans += max(0, leftMax - height[left])
                left += 1
            else:
                ans += max(0, rightMax - height[right])
                right -= 1

        return ans