
# TASK 1: DYNAMIC ARRAY
class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            print("Resizing from", self.capacity, "to", self.capacity * 2)

            new_arr = [None] * (self.capacity * 2)
            for i in range(self.size):
                new_arr[i] = self.arr[i]

            self.arr = new_arr
            self.capacity *= 2

        self.arr[self.size] = x
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Empty"

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def __str__(self):
        return str(self.arr[:self.size])

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# TASK 2: LINKED LIST

# Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def delete(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def traverse(self):
        temp = self.head
        res = []
        while temp:
            res.append(temp.data)
            temp = temp.next
        print(res)


# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = Node(x)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def insert_after(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new = Node(x)

                new.next = temp.next
                new.prev = temp

                if temp.next:
                    temp.next.prev = new

                temp.next = new
                return

            temp = temp.next

        print("Target not found")


    def delete_at_position(self, pos):
        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        while temp and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            return

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        res = []
        while temp:
            res.append(temp.data)
            temp = temp.next
        print(res)

# TASK 3: STACK & QUEUE
class Stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            return "Empty"

        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            return "Empty"
        return self.top.data


class Queue:
    def __init__(self):
        self.front_node = None
        self.rear = None

    def enqueue(self, x):
        new = Node(x)

        if self.rear is None:
            self.front_node = self.rear = new
            return

        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if self.front_node is None:
            return "Empty"

        val = self.front_node.data
        self.front_node = self.front_node.next

        if self.front_node is None:
            self.rear = None

        return val

    def front(self):
        if self.front_node is None:
            return "Empty"
        return self.front_node.data

# TASK 4: PARENTHESES CHECKER
def is_balanced(expr):
    s = Stack()

    for ch in expr:
        if ch in "({[":
            s.push(ch)

        elif ch in ")}]":
            if s.top is None:
                return False

            top = s.pop()

            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return False

    return s.top is None


# TESTING ALL CASES
if __name__ == "__main__":

    print("Task 1: Dynamic Array")
    arr = DynamicArray(2)

    for i in range(1, 12):
        print("Adding:", i)
        arr.append(i)
        print(arr)

    print("\nPopping:")
    print(arr.pop())
    print(arr.pop())
    print(arr.pop())
    print("Final:", arr)


    print("\nTask 2: Singly Linked List")
    sll = SinglyLinkedList()

    sll.insert_beginning(10)
    sll.insert_beginning(20)
    sll.insert_beginning(30)
    sll.traverse()

    sll.insert_end(40)
    sll.insert_end(50)
    sll.insert_end(60)
    sll.traverse()

    sll.delete(20)
    sll.traverse()


    print("\nTask 2: Doubly Linked List")
    dll = DoublyLinkedList()

    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_end(4)
    dll.traverse()

    dll.insert_after(2, 99)
    dll.traverse()

    dll.delete_at_position(1)
    dll.traverse()

    dll.delete_at_position(3)
    dll.traverse()


    print("\nTask 3: Stack")
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)

    print("Peek:", st.peek())
    print("Pop:", st.pop())
    print("Peek:", st.peek())


    print("\nTask 3: Queue")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Front:", q.front())
    print("Dequeue:", q.dequeue())
    print("Front:", q.front())


    print("\nTask 4: Parentheses Checker")
    tests = ["([])", "([)]", "(((", ""]

    for t in tests:
        print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")