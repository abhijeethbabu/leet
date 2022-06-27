# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # no of zeroes == power of 10 == ( pow of 5) + ( pow of 25) + ..
        # a = 0
        # val = len(str(n))+1
        # for p in range(1,val+1):
        #     for i in range(1,n+1):
        #         if i % pow(5,p) == 0:
        #             a += 1
        # return a
        a = 0
        p = 5
        while n//p != 0:
            a += n//p
            p *= 5
        return a



if __name__ == '__main__':
    num = Solution()
    print(num.trailingZeroes(625))