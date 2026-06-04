class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

from_addr = Address(
    index="660000",
    city="Krasnoyarsk",
    street="Tchaikovsky",
    house="11",
    apartment="53"
)

print(from_addr.index)
print(from_addr.city)
print(from_addr.street)
print(from_addr.house)
print(from_addr.apartment)