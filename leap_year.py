def is_leap(year):
  leap=True
  if (year%400==0 and year%100==0) or year%4==0:
    return leap
  else:
    return not leap
year=2100
is_leap(year)
