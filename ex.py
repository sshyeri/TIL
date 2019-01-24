def solve(s):
    if s[0].isalpha():
        s = s.replace(s[0], s[0].upper())
    for i in range(2, len(s)):
        if s[i-1] == ' ' and s[i].isalpha():
           s = s.replace(s[i], s[i].upper())
    return s
print(solve('hello   world  lol'))