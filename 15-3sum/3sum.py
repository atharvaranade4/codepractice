class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i,a in enumerate(nums): #first pointer at 0
            if i > 0 and a == nums[i - 1]: #ensure i and i-1 is diff
                continue
            j = i + 1   #second pointer at index i + 1
            k = len(nums) - 1 #third pointer at the end
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum < 0:
                    j +=1
                elif threeSum > 0:
                    k -=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -=1
                    while j < k and nums[j] == nums[j-1]:
                        j +=1
                    while j < k and nums[k] == nums[k+1]:
                        k -=1
        return ans
                