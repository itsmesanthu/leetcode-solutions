class Solution:
    def intToRoman(self, num: int) -> str:
        dict={
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:"C",
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:"V",
            4:"IV",
            1:"I"
        }
        r=""
        for key,val in dict.items():
            while key<=num:
                r+=val
                num=num-key
            if num<=0:
                break
        return r