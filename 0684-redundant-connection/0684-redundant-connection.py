from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        def has_path(start, target, visited):
            if start == target:
                return True
            visited.add(start)
            for neighbor in graph.get(start, []):
                if neighbor not in visited:
                    if has_path(neighbor, target, visited):
                        return True
            return False
        for u, v in edges:
            visited = set()
            if has_path(u, v, visited):
                return [u, v]
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        return []
