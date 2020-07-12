import re
with open('d://17py//txt//python02_28_02.txt', encoding='gb18030') as f:
    g=f.read()

s = re.findall(r'^\s*\w{5}，\s*\w{5}。\s*$', g, re.MULTILINE)


print(s)