from spiltmilk import *


y = Customer()
time = y.arrivaltime

x = Ticket_line(1)

x.add_customer(y, time)
x.add_customer(y, time)

print(x._queue.front())

print(y)

print(x)
