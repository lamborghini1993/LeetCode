class Solution:
    def intToRoman(self, num: int) -> str:
        lst = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        result = []

        i = 0
        while i < len(lst) and num > 0:
            if num >= lst[i][0]:
                result.append(lst[i][1])
                num -= lst[i][0]
            else:
                i += 1
        return "".join(result)


obj = Solution()
print(obj.intToRoman(3))
print(obj.intToRoman(3749))
print(obj.intToRoman(58))
print(obj.intToRoman(1994))
