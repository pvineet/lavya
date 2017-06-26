class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict ={}
        
        i=0
        for num in nums:
            if target-num in dict:
                return[i, dict[target-num]]
            else:
                dict[num] = i
            i=i+1    

    def twoSumBrute(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)>2:
            for num1 in nums:
                if (target-num1) in nums:
                    if nums.index(num1) != nums.index(target-num1):
                        return [nums.index(num1), nums.index(target-num1)]
                    else:
                        if nums.count(num1)>1:
                            indices = [i for i, x in enumerate(nums) if x==num1]
                            return indices
        else:
            return [0,1]
