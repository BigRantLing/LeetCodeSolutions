# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return head

        secondNode = head.next
        cur_1: ListNode = secondNode
        cur_2 = head

        while cur_1 is not None and cur_1.next is not None:
            cur_2 = cur_2.next
            cur_1 = cur_1.next

        # insert last node after head
        head.next = cur_1
        cur_1.next = secondNode
        cur_2.next = None

        return head


def print_link(head: ListNode):
    curr_node = head

    while curr_node.next is not None:
        print('%d -> ' % curr_node.val, end=' ')
        curr_node = curr_node.next

    print('%d' % curr_node.val)


if __name__ == '__main__':
    ls = [1, 2, 3, 4, 5]

    node = ListNode(ls[0])
    head = node

    for i in range(1, len(ls)):
        next_node = ListNode(ls[i])
        node.next = next_node
        node = node.next

    print_link(head)
    print_link(Solution().reorderList(head))
