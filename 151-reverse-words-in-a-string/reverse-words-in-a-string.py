class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(" ")
        answer = []
        for y in x:
            if y:
                answer.append(y.strip())
        return " ".join(answer[::-1])
        