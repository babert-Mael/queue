#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Queue:
    
    def isEmpty(self):
        """
        Return True if the queue is empty, False otherwise
        """
        raise NotImplementedError
    
    def enqueue(self, element):
        """
        Add an element to the queue.
        Return the queue
        """
        raise NotImplementedError

    def dequeue(self):
        """
        pop the head element of the queue
        return the element
        If the queue is empty, raise IndexError exception.
        """
        raise NotImplementedError

    def head(self):
        """
        return the head of the queue without removing it.
        If the queue is empty, raise IndexError exception.
        """
        raise NotImplementedError

    def size(self):
        """
        read the size of the queue
        return the size as an integer.
        """
        raise NotImplementedError
