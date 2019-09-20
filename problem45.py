class Solution:
    def jump(self, nums: List[int]) -> int:
        jumpnum = current_point = max_point = 0
        for i in range(len(nums)):
            if i > current_point:
                current_point = max_point
                jumpnum +=1
            max_point = max(max_point,i+nums[i])
        return jumpnum