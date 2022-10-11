#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from queue import Queue

class QueueTests(unittest.TestCase):
    """
    A class to test the Queue module
    """
    def setUp(self):
        """
        create an empty queue for all tests
        """
        self.queue=Queue()
    
    def tearDown(self):
        """
        call this at the end of each tests, wheter the test fail or not
        """
        self.queue=Queue()

    def testEnqueue(self):
        """
        Check if the enqueue method works
        """
        element='element'
        self.queue.enqueue(element)
        self.assertTrue(isinstance(self.queue, Queue), "The enqueue method should return an instance of Queue")
        
        
    def testDequeue(self):
        """
        check if the dequeue method works
        """
        elements=['How','are','you','today','?']
        
        for e in elements:
            self.queue.enqueue(e)
        pops=[self.queue.dequeue() for e in elements]
        self.assertEqual(elements, pops, "pops elements should be %s, but we have %s instead."%(elements, pops))
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def testIsEmpty(self):
        """
        Check if the isEmpty method works
        """
        answer1=self.queue.isEmpty()
        self.assertEqual(answer1, True, "isEmpty should be True, it returned %s instead."%answer1)
        element='element'
        self.queue.enqueue(element)
        answer2=self.queue.isEmpty()
        self.assertEqual(answer2, False, "isEmpty should be False, it returned %s instead."%answer2)
        
    def testSize(self):
        """
        Check if the size method works
        """
        size1=self.queue.size()
        self.assertEqual(size1, 0, "size should be 0, it returned %s instead."%size1)
        self.queue.enqueue('test')
        size2=self.queue.size()
        self.assertEqual(size2, 1, "size should be 1, it returned %s instead."%size2)
        self.queue.dequeue()
        size3=self.queue.size()
        self.assertEqual(size3, 0, "size should be 0, it returned %s instead."%size3)
        
    def testHead(self):
        """
        Check if the head method works
        """
        elements=['How','are','you','today','?']
        
        for e in elements:
            self.queue.enqueue(e)
        head1=self.queue.head()
        self.assertEqual(elements[0], head1, "head should be %s, it returned %s instead."%(elements[0], head1))
        self.queue.dequeue()
        head2=self.queue.head()
        self.assertEqual(elements[1], head2, "head should be %s, it returned %s instead."%(elements[1], head2))
        self.queue=Queue()
        with self.assertRaises(IndexError):
            self.queue.head()
        
if __name__ == '__main__':
    unittest.main()        