#!/usr/bin/env python -u
# encoding: utf-8

class Solution():
    def is_palindrome(self,x):
        """
        :type x: int
        :rtype: bool
        """
        print x
        reverse = 0
        while x >0:
            reminder = x % 10
            reverse = (reverse *10) +reminder
            x = x/10
        if x == reverse:
            return True
        else:
            return False

    def is_prime(self,x):
        print x
        reverse = 0
        while x >0:
            reminder = x % 10
            reverse = (reverse *10) +reminder
            x = x/10
        print reverse
        if int(x) != int(reverse):
            return True
        else:
            return False
