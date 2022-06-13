from doublylinkedlist import LinkedList


def removeDups1(ll: LinkedList) -> None:
    """
    This method removes duplicates from a Linked List in O(n) time using O(n) space.
    :param ll: Linked List to remove duplicates from
    :return: None.
    """
    hash_set = set()  # hash set to keep track of data
    itr = ll.head  # linked list iterator
    while itr:  # iterating until at the end of the linked list
        if itr.data not in hash_set:  # data is unique so add to hash set
            hash_set.add(itr.data)
        else:  # duplicate, must remove
            ll.length -= 1  # making sure length is updated correctly
            itr.prev.next = itr.next  # making prev node reference next
            if itr.next:  # if next node exists, making nextnode.prev reference itr.prev
                itr.next.prev = itr.prev
            else:  # if duplicate is in the last position, we must reassign the tail
                ll.tail = itr.prev
        itr = itr.next


def removeDups2(ll: LinkedList) -> None:
    """
    This method removes duplicates from a linked list in O(n^2) time using O(1) space.
    :param ll: Linked list to remove duplicates from
    :return: None.
    """
    itr1 = ll.head  # set first pointer
    while itr1:
        itr2 = itr1.next  # start second pointer at node next to first pointer
        while itr2:  # iterate until at the end of the linked list
            if itr2.data == itr1.data:  # if duplicate
                ll.length -= 1  # decrease length
                itr2.prev.next = itr2.next  # change pointer of prev next to itr2.next
                if itr2.next:  # if itr2.next exists, change pointer of itr2.next.prev
                    itr2.next.prev = itr2.prev
                else:  # itr2.next does not exist so we must update the tail of the linked list
                    ll.tail = itr2.prev
            itr2 = itr2.next  # iterate with 2nd pointer
        itr1 = itr1.next  # iterate with 1st pointer
