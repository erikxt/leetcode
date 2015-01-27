class Solution:
    # @return an integer
    def reverse(self, x):
        res , sign, x = 0, 1 if x > 0 else -1, abs(x)
        while x:
            x, res = x / 10, res * 10 + x % 10
        return 0 if res > pow(2,32) else res * sign
        
def main():
    x =  -132
    s = Solution()
    print s.reverse(x)
        
if __name__ == "__main__":
    main()
