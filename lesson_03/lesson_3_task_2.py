from Smartphone import Smartphone
catalog = []
phone1 = Smartphone("Samsung", "GalaxyS10", "+79321236574")
phone2 = Smartphone("Apple", "Iphone15", "+79834576584")
phone3 = Smartphone("Xiaomi", "15Pro", "+78923587651")
phone4 = Smartphone("Honor", "P12", "+79345673219")
phone5 = Smartphone("Pocco", "S10Ultra", "+78934765293")
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.brend_phone} - {phone.model_phone} . {phone.abonent_number}')