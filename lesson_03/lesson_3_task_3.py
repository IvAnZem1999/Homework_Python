from Address import Address
from Mailing import Mailing
to_addres = Address("777124", "Москва", "Новый Арбат", "5", "11")
from_addres = Address("198432", "Санкт-Петербург", "Ленинский проспект", "20", "67")
mailing = Mailing(to_addres, from_addres, "700", "5673295673728" )
print(mailing)