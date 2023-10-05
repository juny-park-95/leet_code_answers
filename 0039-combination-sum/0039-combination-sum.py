class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                # Skip duplicates to ensure unique combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                # Continue the backtrack with the updated target and path
                backtrack(i, target - candidates[i], path)
                # Backtrack by removing the last element to explore other possibilities
                path.pop()

        candidates.sort()  # Sort candidates to handle duplicates
        result = []
        backtrack(0, target, [])
        return result