#Високосный год
def is_year_leap(year):
  if year % 400 == 0:
    return True
  if year % 4 == 0 and year != 100:
    return True
  return False
  