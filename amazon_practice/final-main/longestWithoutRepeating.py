def longestWithoutRepeating(s):
    n = len(s)
    sett= set()
    left = 0
    maxlen = 0
    for right in range(n):
        while(s[right] in sett):
            sett.remove(s[left])
            left=left+1

        sett.add(s[right])
        maxlen = max(maxlen,right-left+1)
    return maxlen

s = "abcabcdbb"
print(longestWithoutRepeating(s))


