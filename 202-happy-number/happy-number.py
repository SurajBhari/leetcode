class Solution:
    def isHappy(self, n: int) -> bool:
        known_n_iterations = [n]
        while True:
            if n < 0:
                return False
            new_n = 0
            for x in [int(x) for x in list(str(n))]:
                new_n += x**2
            if new_n == 1:
                return True
            else:
                n = new_n
            if n in known_n_iterations:
                return False
            else:
                known_n_iterations.append(n)