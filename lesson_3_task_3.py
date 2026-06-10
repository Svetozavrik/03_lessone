from Address import Address
from Mailing import Mailing

# Создаём адреса
from_addr = Address("123456", "Москва", "Тверская", "15", "123")
to_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "25", "45")

# Создаём экземпляр почтового отправления
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="123456789RU"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
