from singlylinkedlist import LinkedList, Node


def delete_middle_node(n: Node) -> None:
    """
    Delete the middle node of a singly linked list. This code runs in O(1) time
    and has a space complexity of O(1).
    :param n: The node to delete from the singly linked list
    :return: None.
    """
    if not n.next:
        raise AssertionError("Node is not a middle node")
    n.data = n.next.data # copy value from next node to current node
    n.next = n.next.next # delete next node
    
