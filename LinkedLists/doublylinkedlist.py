class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, data) -> None:
        if self.length == 0:
            node = Node(data)
            self.head = node
            self.tail = node
            self.length += 1
            return
        node = Node(data, self.head)
        self.head.prev = node
        self.head = node
        self.length += 1

    def append(self, data) -> None:
        if self.length == 0:
            node = Node(data)
            self.head = node
            self.tail = node
            self.length += 1
            return
        node = Node(data, prev=self.tail)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def insert_values(self, data_list: list) -> None:
        self.clear()
        for data in data_list:
            self.append(data)

    def insert_at(self, index: int, data) -> None:
        if not 0 <= index <= self.length:
            raise AssertionError("Invalid Index")
        if index == 0:
            self.push(data)
            return
        elif index == self.length:
            self.append(data)
            return
        i = 0
        itr = self.head
        stop = index - 1
        while i != stop:
            itr = itr.next
            i += 1
        node = Node(data, itr.next, itr)
        itr.next.prev = node
        itr.next = node
        self.length += 1

    def remove_at(self, index: int) -> None:
        if not 0 <= index < self.length:
            raise AssertionError("Invalid Index")
        if self.length == 1:
            self.clear()
            return
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        i = 0
        itr = self.head
        while i != index-1:
            itr = itr.next
            i += 1
        itr.next = itr.next.next
        itr.next.prev = itr
        self.length -= 1
        return

    def insert_after_value(self, data_after, data_insert) -> None:
        index = self.index(data_after)
        if index == -1:
            raise AssertionError("Data not found in Linked List")
        self.insert_at(index + 1, data_insert)

    def remove_by_value(self, data) -> None:
        index = self.index(data)
        if index == -1:
            raise AssertionError("Data not found in Linked List")
        self.remove_at(index)

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def index(self, data) -> int:
        if self.length == 0:
            return -1
        index = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return index
            index += 1
            itr = itr.next
        return -1

    def __str__(self) -> str:
        if self.length == 0:
            return "Linked List is Empty"
        ll = []
        itr = self.head
        while itr:
            ll.append(str(itr.data))
            ll.append("-->")
            itr = itr.next
        ll.append("None")
        return "".join(ll)

    def print_backward(self) -> str:
        if self.length == 0:
            return "Linked List is Empty"
        ll = list()
        ll.append("None")
        itr = self.tail
        while itr:
            ll.append("<--")
            ll.append(str(itr.data))
            itr = itr.prev
        return "".join(ll)

    def __contains__(self, item) -> bool:
        if self.length == 0: return False
        itr = self.head
        while itr:
            if itr.data == item: return True
            itr = itr.next
        return False

    def __len__(self) -> int:
        return self.length
