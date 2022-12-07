class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return "Zero"

        num = str(num)[::-1]
        n = len(num)
        res = []
        wordMap = {"0": "", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
                   "7": "Seven", "8": "Eight", "9": "Nine", "10": "Ten", "11": "Eleven", "12": "Twelve",
                   "13": "Thirteen", "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen",
                   "18": "Eighteen", "19": "Nineteen", "20": "Twenty", "30": "Thirty", "40": "Forty", "50": "Fifty",
                   "60": "Sixty", "70": "Seventy", "80": "Eighty", "90": "Ninety"}
        i = n - 1
        while i >= 0:
            if i % 3 == 0:
                res.append(wordMap[num[i]])
            elif i % 3 == 1:
                if int(num[i]) > 1:
                    res.append(wordMap[num[i] + "0"])
                    res.append(wordMap[num[i - 1]])
                else:
                    res.append(wordMap[num[i] + num[i-1]])

                i -= 1

            elif i % 3 == 2:
                res.append(wordMap[num[i]])
                res.append("Hundred")

            if i == 9:
                res.append("Billion")
            if i == 6:
                res.append("Million")
            if i == 3:
                res.append("Thousand")

            i -= 1
        return ' '.join(res) if res[-1] != "" else ' '.join(res[:-1])


test = Solution()
a = 20
r = test.numberToWords(a)
print(10)

