from Address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

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

print(to_addr.index)
print(to_addr.city)
print(to_addr.street)
print(to_addr.house)
print(to_addr.apartment)
print(mailing.cost)
print(mailing.track)
