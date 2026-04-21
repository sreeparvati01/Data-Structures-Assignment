# TASK 1
# BST IMPLEMENTATION

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False

        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # No child
            if node.left is None and node.right is None:
                return None

            # One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Two children
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


def test_bst():
    bst = BST()
    print("\nBST TESTING")

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Initial Inorder:", bst.inorder())

    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    bst.delete(20)
    print("After deleting leaf (20):", bst.inorder())

    bst.insert(65)
    bst.delete(60)
    print("After deleting node with one child (60):", bst.inorder())

    bst.delete(30)
    print("After deleting node with two children (30):", bst.inorder())



#TASK 2
#GRAPH IMPLEMENTATION 

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        print("\nAdjacency List:")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        print("\nBFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor, _ in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start):
        visited = set()
        print("\nDFS Traversal:", end=" ")
        self._dfs(start, visited)

    def _dfs(self, node, visited):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor, _ in self.graph.get(node, []):
                self._dfs(neighbor, visited)


def test_graph():
    g = Graph()
    print("\nGRAPH TESTING")

    edges = [
        ('A', 'B', 2),
        ('A', 'C', 4),
        ('B', 'D', 7),
        ('B', 'E', 3),
        ('C', 'E', 1),
        ('D', 'F', 5),
        ('E', 'D', 2),
        ('E', 'F', 6),
        ('C', 'F', 8)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    g.print_graph()
    g.bfs('A')
    g.dfs('A')

#TASK 3
#HASH TABLE IMPLEMENTATION

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


def test_hash_table():
    print("\nHASH TABLE TESTING")

    ht = HashTable(5)

    data = [(10, "A"), (15, "B"), (20, "C"), (7, "D"), (12, "E")]

    for k, v in data:
        ht.insert(k, v)

    ht.display()

    print("\nRetrieve 10:", ht.get(10))
    print("Retrieve 7:", ht.get(7))
    print("Retrieve 12:", ht.get(12))

    print("\nDeleting key 15 (collision bucket)...")
    ht.delete(15)

    ht.display()



if __name__ == "__main__":
    print("\nDMMT TOOLKIT OUTPUT")

    test_bst()
    test_graph()
    test_hash_table()

    