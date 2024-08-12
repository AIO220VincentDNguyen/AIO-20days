from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def bfs(self):
        if not self.root:
            return []
        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def search(self, value):
        if not self.root:
            return False
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    def delete(self, value):
        if not self.root:
            return False
        queue = deque([self.root])
        node_to_delete = None
        last_node = None
        parent_of_last_node = None

        while queue:
            node = queue.popleft()
            if node.value == value:
                node_to_delete = node
            if node.left:
                parent_of_last_node = node
                queue.append(node.left)
                last_node = node.left
            if node.right:
                parent_of_last_node = node
                queue.append(node.right)
                last_node = node.right

        if node_to_delete:
            if last_node:
                node_to_delete.value = last_node.value
                if parent_of_last_node.left == last_node:
                    parent_of_last_node.left = None
                else:
                    parent_of_last_node.right = None
            else:
                self.root = None
            return True
        return False
# Create Tree
tree = Tree()

# add value
tree.insert(9)
tree.insert(10)
tree.insert(15)
tree.insert(8)
tree.insert(7)
tree.insert(11)
tree.insert(17)

# print (BFS)
print("BFS:", tree.bfs())  # Expected: [10, 5, 15, 3, 7, 12, 18]

# search value
print("Search 7:", tree.search(7))  # Expected: True
print("Search 20:", tree.search(20))  # Expected: False

# insert value
tree.insert(20)
print("BFS after inserting 20:", tree.bfs())  # Expected: [10, 5, 15, 3, 7, 12, 18, 20]

# delete value
tree.delete(10)
print("BFS after deleting 10:", tree.bfs())  # Expected: [18, 5, 15, 3, 7, 12, 20]