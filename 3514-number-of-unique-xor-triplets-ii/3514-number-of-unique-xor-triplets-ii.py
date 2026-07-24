class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX_XOR = 2048
        n = len(nums)
        pair_xor = [False] * MAX_XOR
        for i in range(n):
            for j in range(i, n):
                pair_xor[nums[i] ^ nums[j]] = True
        triplet_xor = [False] * MAX_XOR
        for x in range(MAX_XOR):
            if pair_xor[x]:
                for num in nums:
                    triplet_xor[x ^ num] = True
        return sum(triplet_xor)