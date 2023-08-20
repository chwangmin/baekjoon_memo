import re
input()
s = input()
print(sum(map(int, re.findall('[0-9]+',s))))