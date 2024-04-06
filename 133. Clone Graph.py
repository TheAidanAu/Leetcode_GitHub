class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # recursive clone function, hashmap for visited nodes
        if not node:
            return None

        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node)

# time: O(edges + nodes)