def is_year_leap(year):
     if (year % 4 == 0):
          print(f"Year: {year} - True")
     else :
          print(f"Year: {year} - False")
is_year_leap(int(input("Введите год: ")))