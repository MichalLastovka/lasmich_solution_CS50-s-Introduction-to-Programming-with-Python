"""
Task:
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:

    __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
    __str__ should return a str with 

🍪, where

    is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
    withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
    capacity should return the cookie jar’s capacity.
    size should return the number of cookies actually in the cookie jar.

Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.

"""


class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size


    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number has to be non-negative integer")
        elif (n + self.size) > self.capacity:
            raise ValueError("Out of jar's capacity")
        self.size += n


    def withdraw(self, n):
        if  n < 0:
            raise ValueError("Number has to be non-negative integer")
        elif self.size - n < 0:
            raise ValueError("Withdrawl is greater than current number of cookies stored")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity has to be non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Out of jar's capacity")
        self._size = size
