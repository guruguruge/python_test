from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target - num], i]
        hash_map[num] = i
    return []

# テスト
if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))  # -> [0,1]