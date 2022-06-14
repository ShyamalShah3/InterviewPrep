class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None  # points to the head of the list
        self.length = 0  # keeps track of the length of the list for optimization purposes

    def push(self, data) -> None:
        """
        Adds an element to the front of the linked list
        :param data: data to insert into the linked list
        :return: None.
        """
        new_node = Node(data, self.head)
        self.head = new_node
        self.length += 1

    def append(self, data) -> None:
        """
        Adds an element to the end of the linked list
        :param data:
        :return: None.
        """
        self.length += 1
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return

    def insert_values(self, data_list: list) -> None:
        """

        :param data_list:
        :return:
        """
        self.clear()
        i = len(data_list) - 1
        while i >= 0:
            self.push(data_list[i])
            i -= 1

    def insert_at(self, index: int, data):
        """
        Inserts data into the Linked List at the specified index.
        :param index: 0 <= index <= self.length, index where to insert data
        :param data: data to insert
        :return: None.
        """
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
        itr.next = Node(data, itr.next)
        self.length += 1

    def insert_after_value(self, data_after, data_to_insert) -> None:
        if data_after not in self: raise AssertionError("Data not found in Linked List")
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                self.length += 1
                break
            itr = itr.next

    def remove_by_value(self, data) -> Node:
        """

        :param data: Value to remove from the linked list
        :return: Node representing
        """
        if data not in self: raise AssertionError("Data not found in Linked List")
        self.length -= 1
        if self.head.data == data:
            removed = self.head
            self.head = self.head.next
            return removed
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                removed = itr.next
                itr.next = itr.next.next
                return removed
            itr = itr.next

    def remove_at(self, index: int) -> None:
        """
        Removes the element at the specified index.
        :param index: 0 <= index <= self.length, index where to remove data
        :return: None.
        """
        if not 0 <= index < len(self):
            raise AssertionError("Invalid Index")

        self.length -= 1
        if index == 0:
            self.head = self.head.next
            return

        i = 0
        itr = self.head
        stop = index - 1
        while i != stop:
            itr = itr.next
            i += 1
        itr.next = itr.next.next

    def __contains__(self, data) -> bool:
        """
        Determines if an element is present in the Linked List
        :param data: data to find in the linked list
        :return: True if data in Linked List. False Otherwise
        """
        if self.length == 0: return False
        found = False
        itr = self.head
        while itr:
            if itr.data == data:
                found = True
                break
            itr = itr.next
        return found

    def __len__(self) -> int:
        """
        Gets the length of the Linked List
        :return: The length of the linked list
        """
        return self.length

    def __str__(self) -> str:
        """
        Converts Linked List into string representation
        :return: String representation of the linked list
        """
        if self.head is None:
            return "Linked List is Empty"

        llstr = []
        itr = self.head

        while itr:
            llstr.append(str(itr.data))
            llstr.append("-->")
            itr = itr.next
        llstr.append("None")
        return "".join(llstr)

    def clear(self) -> None:
        """
        Clears the Linked List
        :return: None.
        """
        self.head = None
        self.length = 0