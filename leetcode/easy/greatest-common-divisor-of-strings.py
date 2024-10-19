class Solution:
    def gcd(x1: int, x2: int):
        factor = 2
        gcd = 1
        while factor <= x1 and factor <= x2:
            if x1 % factor == 0 and x2 % factor == 0:
                gcd *= factor
                x1 = x1 // factor
                x2 = x2 // factor
            elif x1 % factor == 0:
                x1 = x1 // factor
            elif x2 % factor == 0:
                x2 = x2 // factor
            else:
                factor += 1
            
        return gcd

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        greatest = gcd(len(str1), len(str2))
        if (str2 in str1 or str1 in str2) and (len(str1) // greatest) * str2[:greatest] == str1:
            return str2[:greatest]
        return ''