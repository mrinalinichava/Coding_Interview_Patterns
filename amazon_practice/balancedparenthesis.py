class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if (n % 2 != 0):
            return False

        for i in range(n):
            if (s[i] in ['(', '{', '[']):
                stack.append(s[i])
            else:
                if (not stack):
                    return False
                top_ele = stack.pop()
                if (s[i] == ')' and top_ele != '('):
                    return False
                if (s[i] == '}' and top_ele != '{'):
                    return False
                if (s[i] == ']' and top_ele != '['):
                    return False
        if (stack):
            return False
        else:
            return True

soln = Solution()
string1 ="((()))"
print(soln.isValid(string1))