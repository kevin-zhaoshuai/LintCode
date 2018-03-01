class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

