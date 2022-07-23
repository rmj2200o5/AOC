import re
with open("C:/Users/Robert J/VS Code/PythonWorks/AdventOfCode/2015/day05in.txt") as ipt:
    strings = ipt.read().splitlines()
print(len([string for string in strings if (re.search(r"(.*[aeiou]){3}",string)) and (re.search(r"(.)\1",string)) and not (re.search(r"ab|cd|pq|xy",string))]))
print(len(strings))
print(len([string for string in strings if re.search(r"(..).*\1",string) and re.search(r"(.).\1",string)]))