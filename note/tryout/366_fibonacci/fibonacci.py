class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        # range(1, n+1) will 1 to n.
        # f(n) = f(n-1)+f(n-2)
        a = 0
        b = 1
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            for i in range(3, n+1):
                c = a + b
                a = b
                b = c
        return c

