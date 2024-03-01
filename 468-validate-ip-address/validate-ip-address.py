class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ":" in queryIP:
            splitted = queryIP.split(":")
            if len(splitted) != 8:
                return "Neither"
            for n in splitted:
                try:
                    i = int(n,16)
                except ValueError:
                    return "Neither"
                if len(n) > 4:
                    return "Neither"
                if not n:
                    return "Neither"
            return "IPv6"
        else:
            # check for ipv4
            splitted = queryIP.split(".")
            if len(splitted) != 4:
                return "Neither"
            for n in splitted:
                if n.startswith("0") and n != "0":
                    return "Neither"
                if not n:
                    return "Neither"
                if not n.isnumeric():
                    return "Neither"
                i = int(n)
                if i<0 or i > 255:
                    return "Neither"
            return "IPv4"
        