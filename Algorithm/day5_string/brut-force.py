
def strbf(pattern, text):
    i, j = 0, 0
    m, n = len(pattern), len(text)
    while j < m and i < n:
        if text[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j==m :
        return i-m
    else:
        return -1
pattern = input()
text = input()
print(strbf(pattern, text)    )
    