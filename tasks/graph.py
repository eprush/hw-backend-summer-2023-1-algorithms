from typing import Any
from queue import Queue
__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        def recursive_dfs(node, res):
            if node not in res:
                res.append(node)
                for other in node.outbound:
                    recursive_dfs(other, res)
            return

        result = [self._root]
        for node in self._root.outbound:
            recursive_dfs(node, result)
        return result



    def bfs(self) -> list[Node]:
        result = []
        stack  = [self._root]
        while stack:
            if stack[-1] not in result:
                node = stack.pop()
                result.append(node)
                stack = node.outbound[::-1] + stack
            else:
                stack.pop()

        return result
