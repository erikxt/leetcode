class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        return self.find(num, range(0, len(num)))        
    
    def find(self, num, args):
        if len(args) == 1:
            return args[0]            
        elif len(args) == 2:
            if num[args[0]] >= num[args[1]]:
                    return args[0]
            else:
                    return args[1]                
        else:
            m = len(args)
            n = m / 2
            a = self.find(num, args[0:n])
            b = self.find(num, args[n: m])
            if (num[a] >= num[b]):
                    return a
            else:
                    return b        


def main():
    num = [1,2,3,5,3,6,2,3,2,2,3,5,3,6,2,3,2,2,3,5,3,6,2,3,2,2,3,5,3,6,2,3,2,2,3,5,3,6,2,3,2,2,3,5,3,6,2,3,2]
    s = Solution()
    before = time.time()
    print s.findPeakElement(num)
        
if __name__ == "__main__":
    main()

