"""
Leetcode 209.长度最小的子数组

解题思路：
滑动窗口，时间复杂度O(n)(代码参考：灵茶山艾府）
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n=len(nums)
        ans=n+1
        s=0
        left=0
        for right,x in enumerate(nums):
            s+=x
            while s-nums[left]>=target:
                s-=nums[left]
                left+=1
            if s>=target:
                ans=min(ans,right-left+1)
        return ans if ans<=n else 0
