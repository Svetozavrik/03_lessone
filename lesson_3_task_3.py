from Address import Address
from Mailing import Mailing

from_addr = Address(
    index="660000",
    city="Krasnoyarsk",
    street="Tchaikovsky",
    house="11",
    apartment="53"
)

to_addr = Address(
    index="603000",
    city="Mosсow",
    street="Alexander Solzhenitsyn",
    house="23A",
    apartment="2"
)


mailing = Mailing(
    to_address=to_addr,
    from_address=Mailing, 
    cost=500,
    track="RU123456789RU"
)

print(from_addr.index)
print(from_addr.city)
print(from_addr.street)
print(from_addr.house)
print(from_addr.apartment)
print(to_addr.index)
print(to_addr.city)
print(to_addr.street)
print(to_addr.house)
print(to_addr.apartment)
print(mailing.cost)
print(mailing.track)
