class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        cursum = numbers[i] + numbers[j]
        while cursum != target:
            if cursum > target:
                j = j - 1
            elif cursum < target:
                i = i + 1
            cursum = numbers[i] + numbers[j]
        return [i + 1, j + 1]