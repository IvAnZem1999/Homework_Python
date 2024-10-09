def month_of_season(month):
    if month in [1, 2, 12]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"
month = int(input("Введите номер месяца (1-12):"))
print (f"Сезон: {month_of_season(month)}")