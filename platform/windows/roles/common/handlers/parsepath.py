# /usr/bin/python3

import sys, re

if re.search(r'u0007', sys.argv[1]):
    p = sys.argv[1].split('\\')
    s = "/".join(p)
    out = s.replace("u0007",'a')
    print(out)
else:
    s = sys.argv[1]
    p =s.split('\\')
    del p[:3]
    out = "/".join(p)
    print(out)
