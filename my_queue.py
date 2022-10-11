#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
class Queue:
    
    def __init__(self):
        self._element=deque()
    
    def isEmpty(self):
        """
        Return True if the queue is empty, False otherwise
        """
        return len(self._element)==0
    
    def enqueue(self, element):
        """
        Add an element to the queue.
        Return the queue
        """
        self._element.appendleft(element)
        return self._element

    def dequeue(self):
        """
        pop the head element of the queue
        return the element
        If the queue is empty, raise IndexError exception.
        """
        return self._element.pop()

    def head(self):
        """
        return the head of the queue without removing it.
        If the queue is empty, raise IndexError exception.
        """
        return self._element[-1]

    def size(self):
        """
        read the size of the queue
        return the size as an integer.
        """
        return len(self._element)
