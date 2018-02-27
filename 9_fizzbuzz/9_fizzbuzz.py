class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        list = []
        for i in range(1, n+1):
            if i%15 == 0 :
                list.append("fizz buzz")
            elif i%3 == 0:
                list.append("fizz")
            elif i%5 == 0:
                list.append("buzz")
            else:
                list.append(str(i))
                
        return list
        
