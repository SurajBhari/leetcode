class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            clean_pass = True
            i = 0
            while i < len(s):   
                try:
                    stmt1 = s[i].upper() == s[i+1]
                    stmt2 = s[i] == s[i+1].upper()
                    stmt3 = s[i] == s[i+1]
                    if ((stmt1) or (stmt2)) and not stmt3:
                        clean_pass = False
                        s = s.replace(s[i]+s[i+1], "")
                except IndexError:
                    break
                i += 1
            if clean_pass:
                break
        return s