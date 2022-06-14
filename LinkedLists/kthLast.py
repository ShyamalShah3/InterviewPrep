from singlylinkedlist import LinkedList
from singlylinkedlist import Node


def kth_last(k: int, ll: LinkedList) -> Node:
    """
    This method returns the kth to last node in the singly linked list, ll.
    :param k: The kth to last node to find in the Linked List, ll. 1 < k <= len(ll)
    :param ll: The Singly Linked List to find the kth last value in.
    :return: The kth to last node in the Linked List, ll.
    """
    if not 0 < k <= len(ll):  # checking if k is valid.
        raise AssertionError("Invalid value of k")
    # Assuming we do not have access to the length of the linked list
    offset = k - 1  # calculating offset of the front pointer
    fptr = ll.head
    while offset > 0:  # offsetting the front pointer
        fptr = fptr.next
        offset -= 1
    kptr = ll.head
    while fptr.next:  # when fptr.next reaches the end, node at kptr will be the kth last node
        fptr = fptr.next
        kptr = kptr.next
    return kptr
