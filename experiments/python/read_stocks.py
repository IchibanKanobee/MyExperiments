#s[s.find("(")+1:s.find(")")]

fname = "canadian_cannabis.html"

with open(fname) as f:
    s = f.read()

print s

stocks = s[s.find("(")+1:s.find(")")]
print stocks
