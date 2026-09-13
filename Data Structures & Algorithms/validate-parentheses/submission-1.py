class Solution:
    def isValid(self, s: str) -> bool:
        val = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        pars = []
        for p in s:
            if p in val:
                pars.append(p)
            elif len(pars) > 0 and p == val[pars[-1]]:
                pars.pop()
            else:
                return False
        if len(pars) > 0:
            return False
        return True