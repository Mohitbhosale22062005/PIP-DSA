# structure.py

# ================= ARRAY =================
class Array:
    def __init__(self, data=[]):
        self.data = data

    def insert(self, value):
        self.data.append(value)
        return self

    def delete(self, value):
        if value in self.data:
            self.data.remove(value)
        return self

    def sort(self, method='quick'):
        if method == 'quick':
            self.data = Sorting.quick_sort(self.data)
        elif method == 'bubble':
            self.data = Sorting.bubble_sort(self.data)
        return self

    def display(self):
        print("Array:", self.data)
        return self

# ================= LINKED LIST =================
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        return self

    def delete(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                break
            prev = curr
            curr = curr.next
        return self

    def display(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        print("LinkedList:", res)
        return self

# ================= STACK =================
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        return self

    def pop(self):
        if self.stack:
            self.stack.pop()
        return self

    def display(self):
        print("Stack:", self.stack)
        return self

# ================= QUEUE =================
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        return self

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
        return self

    def display(self):
        print("Queue:", self.queue)
        return self

# ================= GRAPH =================
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, directed=False):
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)
        return self

    def bfs(self, start):
        visited = [False]*self.n
        queue = [start]
        visited[start] = True
        order = []
        while queue:
            node = queue.pop(0)
            order.append(node)
            for neigh in self.adj[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    queue.append(neigh)
        print("BFS order:", order)
        return self

    def dfs_util(self, node, visited, order):
        visited[node] = True
        order.append(node)
        for neigh in self.adj[node]:
            if not visited[neigh]:
                self.dfs_util(neigh, visited, order)

    def dfs(self, start):
        visited = [False]*self.n
        order = []
        self.dfs_util(start, visited, order)
        print("DFS order:", order)
        return self

# ================= SORTING =================
class Sorting:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return Sorting.quick_sort(left) + [pivot] + Sorting.quick_sort(right)

    @staticmethod
    def display(arr):
        print("Sorted Array:", arr)
        return arr

# ================= SEARCHING =================
class Searching:
    @staticmethod
    def linear_search(arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1

    @staticmethod
    def binary_search(arr, target):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

================= BINARY SEARCH TREE =================

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a node into the BST"""
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = BSTNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = BSTNode(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        """Search for a key in BST"""
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def inorder(self):
        """Inorder traversal"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

    def preorder(self):
        """Preorder traversal"""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, root, result):
        if root:
            result.append(root.key)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def postorder(self):
        """Postorder traversal"""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._postorder(root.right, result)
            result.append(root.key)

# ================= DEMO =================
if __name__ == "__main__":
    print("=== Array Demo ===")
    arr = Array([5,3,8,1])
    arr.display().sort().display().insert(10).display()

    print("\n=== LinkedList Demo ===")
    ll = LinkedList()
    ll.insert(5).insert(3).insert(8).display().delete(3).display()

    print("\n=== Stack & Queue Demo ===")
    st = Stack().push(5).push(3).push(8).display().pop().display()
    q = Queue().enqueue(1).enqueue(2).enqueue(3).display().dequeue().display()

    print("\n=== Graph Demo ===")
    g = Graph(5)
    g.add_edge(0,1).add_edge(0,2).add_edge(1,3).add_edge(3,4)
    g.bfs(0).dfs(0)

    print("\n=== Sorting & Searching Demo ===")
    sorted_arr = Sorting.quick_sort([5,3,8,1])
    Sorting.display(sorted_arr)
    print("Linear Search for 8:", Searching.linear_search(sorted_arr, 8))
    print("Binary Search for 1:", Searching.binary_search(sorted_arr, 1))
bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("Inorder:", bst.inorder())     # [20, 30, 40, 50, 60, 70, 80]
    print("Preorder:", bst.preorder())   # [50, 30, 20, 40, 70, 60, 80]
    print("Postorder:", bst.postorder()) # [20, 40, 30, 60, 80, 70, 50]

    print("Search 60:", bst.search(60))   # True
    print("Search 100:", bst.search(100)) # False