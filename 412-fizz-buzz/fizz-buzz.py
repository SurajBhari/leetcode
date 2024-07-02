class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for x in range(1,n+1):
            if x%15==0:
                l.append("FizzBuzz")
                continue
            elif x%5==0:
                l.append("Buzz")
                continue
            elif x%3==0:
                l.append("Fizz")
                continue
            else:
                l.append(str(x))
        return l
