class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for o in logs:
            if o.startswith(".."):
                if depth > 0:
                    depth -= 1
            elif o.startswith("."):
                pass
            else:
                depth += 1
        return depth
        