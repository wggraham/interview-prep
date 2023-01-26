from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(i) for i in range(1, n + 1)]

        for i in range(1, n + 1):
            c = ""
            if not i % 3:
                c = "Fizz"
            if not i % 5:
                c += "Buzz"
            ans[i - 1] = c if c else ans[i - 1]
        return ans

    def fizzBuzz2(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            c = ""
            if not i % 3:
                c = "Fizz"
            if not i % 5:
                c += "Buzz"
            ans += [c] if c else [str(i)]
        return ans

    def fizzBuzz3(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                ans.append("FizzBuzz")
            elif not i % 3:
                ans.append("Fizz")
            elif not i % 5:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans

    def fizzBuzz4(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            match i:
                case _ if not i % 3 and not i % 5:
                    ans.append("FizzBuzz")
                case _ if not i % 3:
                    ans.append("Fizz")
                case _ if not i % 5:
                    ans.append("Buzz")
                case _:
                    ans.append(str(i))

        return ans

    def fizzBuzz5(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            match i:
                case _ if not i % 3 and not i % 5:
                    ans += ["FizzBuzz"]
                case _ if not i % 3:
                    ans += ["Fizz"]
                case _ if not i % 5:
                    ans += ["Buzz"]
                case _:
                    ans.append(str(i))

        return ans

    def fizzBuzz6(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 and i % 5:
                ans += [str(i)]
                continue

            ans += [''.join(c for v, c in [(3, "Fizz"), (5, "Buzz")] if not i % v)]

        return ans

    def fizzBuzz8(self, n: int) -> List[str]:
        return [str(i) if i % 3 and i % 5 else ''.join(c for v, c in [(3, "Fizz"), (5, "Buzz")] if not i % v)
                for i in range(1, n + 1)]

    def fizzBuzz7(self, n: int) -> List[str]:
        ans = [str(i) for i in range(1, n + 1)]
        for i in range(1, n + 1):
            if i % 3 and i % 5: continue
            ans[i - 1] = ""
            for v, c in [(3, "Fizz"), (5, "Buzz")]:
                if i % v: continue
                ans[i - 1] += c

        return ans


n = 15
test = Solution()
print(test.fizzBuzz(n))
print(test.fizzBuzz2(n))
print(test.fizzBuzz3(n))
print(test.fizzBuzz4(n))
print(test.fizzBuzz5(n))
print(test.fizzBuzz8(n))
