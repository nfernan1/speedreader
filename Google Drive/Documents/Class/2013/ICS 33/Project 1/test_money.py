from ccmodule import Money

m = Money('USD', 2011)
n = Money('JPY', 2011)

print(type(n.getmoney()))
j = m + n
l = m - n
print(j)
print(l)
