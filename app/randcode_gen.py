import random

class RandcodeGen:
    """進位轉換器
    """
    def __init__(self,char) -> None:
        self.char = char
        self.charLen = len(char)

    def int2str(self, value:int) -> str:
        """回傳進位轉換的值
        Args: value (int): 數值
        Returns: str: 轉換後的值
        """
        output = ""
        while value > self.charLen:
            (value,c) = divmod(value,self.charLen)
            output = self.char[c] + output

        output = self.char[value] + output
        return output
    
    def random(self, length:int) -> str:
        """回傳指定長度的隨機值
        Args: length (int): 長度
        Returns: str: 隨機值
        """
        output = ""
        for i in range(length):
            output += self.int2str(random.randint(0, self.charLen-1))
        return output
    
    def Base36():
        """取36進位的轉換器
        """
        return RandcodeGen('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    


