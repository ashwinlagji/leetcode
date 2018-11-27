# Unoptimized
# Runtime: 96 ms, faster than 19.78% of Python3 online submissions for String to Integer (atoi).


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        x = self.getInt(str)
        
        MAX_32_bit_integer = (1 << 31)-1
        MIN_32_bit_integer = (-1 << 31)
        if x > MAX_32_bit_integer: 
            return MAX_32_bit_integer

        elif MIN_32_bit_integer > x:        
            return MIN_32_bit_integer
        else:
            return x
        
    
    def getInt(self,num):
        
        out = ""
        isNegative = False
        isPositive = False
        for i in num:
            
            if (i == " "):
                if len(out)>0 or isNegative == True or isPositive == True:
                    break
            elif i.isalpha():
                break
            elif (i == "-" or i == "+"):

                if (isNegative == True or isPositive == True ):
                    out = "0"
                    break
                elif i == "-" and isNegative == False and isPositive == False and len(out)==0:
                    isNegative = True
                    continue
                elif i == "+" and isPositive == False and isNegative == False and len(out)==0:
                    isPositive = True
                    continue
                elif ( isNegative == True or isPositive == True or len(out)!=0):
                    break
            else:
                out +=i
        out = out if len(out)>0 else "0"    
        return -(self.getNumber(out)) if isNegative else self.getNumber(out)
    def getNumber(self,s):
        try:
            return int(s)
        except ValueError:
            return int(float(s))