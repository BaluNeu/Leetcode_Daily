class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        new_n = bin(n)
        new_n = int(new_n[2:])
        print(new_n)
        if new_n % (10**(len(str(new_n)) - 1)) == 0:
            return True
        else:
            return False
        
        