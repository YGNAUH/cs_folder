def strStr(haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0
    if needle in haystack:
        for i in range(0,len(haystack),len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
    else:
        return -1

print(strStr(haystack = "hello", needle = "ll"))