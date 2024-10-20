from address import Address
from mailing import Mailing

to_address = Address("101000", "Москва", "Арбат", "12", "45")
from_address = Address("123456", "Санкт-Петербург", "Невский проспект", "56", "12")

mailing = Mailing(to_address, from_address, 350, "TRACK123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")