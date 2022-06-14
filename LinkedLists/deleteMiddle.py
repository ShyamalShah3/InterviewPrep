from singlylinkedlist import LinkedList, Node


def delete_middle_node(n: Node) -> None:
    """
    Delete the middle node of a singly linked list. This code runs in O(n) time
    and has a space complexity of O(1).
    :param n: The node to delete from the singly linked list
    :return: None.
    """
    itr = n  # iterator
    while itr.next.next:  # while we are not at the node previous to the last node
        itr.data = itr.next.data  # copy data from next node to current node
        itr = itr.next
    itr.data = itr.next.data  # copy data from last node to current node
    itr.next = None  # delete the last node
