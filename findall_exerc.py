import re
fh = open(name)

print " "
key = 0
for line in fh:
        line = line.rstrip()
        y = re.findall('^"ads_lift',line)
        if y <> []:
              print y, "is extracted from line:", line

