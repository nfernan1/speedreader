from ccmodule import Currency

Cur = Currency()

converted = Cur.baseline_conversion('JPY', 2011)

print(converted)

print(Cur.convertback('USD', 20.52))
