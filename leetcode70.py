import sys

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        steps = 0
        if n == 0:
            return 1
        if n - 1 >= 0:
            # print "step1" + str(n)
            # print "step1x" + str(n) + " : " + str(Solution().climbStairs(n-1))
            steps += Solution().climbStairs(n - 1)
        if n -2 >= 0:
            # print "step2" + str(n)
            # print "step2x" + str(n) + " : " + str(Solution().climbStairs(n-2))
            steps += Solution().climbStairs(n - 2)

        return steps

    def climbStairs_f(self, n):
        """
        :type n: int
        :rtype: int
        using fibonacci
        """

        a = 1
        b = 0
        while n:
            a,b = a + b, a
            n -= 1

        return a

    def climbStairs_f2(self, n):
        """
        :type n: int
        :rtype: int
        using fibonacci
        """

        a = b = 1
        for _ in range(n):
            a,b = b, a + b

        return a

print Solution().climbStairs_f(int(sys.argv[1]))
