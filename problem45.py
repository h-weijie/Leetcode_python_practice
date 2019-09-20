class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = [0]
        end = len(nums)
        i = 1 
        length = last = 0
        while i<end:
            start = queue[0]
            if i <= start + nums[start]:
                queue.append(i)
                i += 1
            else:
                if last == queue.pop(0):
                    last = queue[-1]
                    length += 1
            if i == end:
                length += 1
                break
        return length