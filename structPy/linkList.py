#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, item):
        # 存储数据
        self.item = item
        # 存储引用
        self.next = None


class SingleLinkList(object):
    """单链表

    Args:
        object (_type_): _description_
    """

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """
        Summary:
        Check if the linked list is empty.

        Explanation:
        This function checks if the linked list is empty
        by verifying if the head node is None.

        Args:
        - self

        Returns:
        bool: True if the linked list is empty, False otherwise.
        """

        return self.__head is None

    def length(self):
        """
        Summary:
        Calculate the length of the linked list.

        Explanation:
        This function iterates through the linked list nodes to count
        the number of elements and returns the total length.

        Args:
        - self

        Returns:
        int: The number of elements in the linked list.
        """

        cur = self.__head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.item, end=" ")
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """
        Summary:
        Append a new node with the given item to the end of the linked list.

        Explanation:
        This function creates a new node with the provided item
        and appends it to the end of the linked list. If the list is empty,
        the new node becomes the head; otherwise, it is added after the
        last node.

        Args:
        - item: The data to be stored in the new node.

        Returns:
        None
        """

        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        cur = self.__head


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    ll.append(1)
    ll.travel()
    print(ll.is_empty(), ll.length())
    for x in range(10):
        ll.append(x)
    ll.travel()
