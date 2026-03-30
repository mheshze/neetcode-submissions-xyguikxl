class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for x in s:
            if x in '}])':
                if res:
                    if (x == '}' and res[-1] == '{') or (x == ')' and res[-1] == '(') or (x == ']' and res[-1] == '['):
                        res.pop()
                    else:
                        return False
                else:
                    return False
            else:
                res.append(x)
        return len(res) == 0

        
        

            