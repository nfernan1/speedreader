from ccmodule import Credit_card
from ccmodule import Money

CC = Credit_card('USD', Money('USD', 0), Money('USD', 2000))

CC.purchase(Money('USD', 30))


print(CC)

LL = Credit_card('USD', Money('USD', 0), Money('USD', 2000))

LL.purchase(Money('USD',400))
LL.payment(Money('USD',300))

print(LL)
