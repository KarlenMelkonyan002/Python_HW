def square_of_greaters(a, b, c):
  if a <= b and a <= c:
    return (b**2) + (c**2)
  elif b <= a and b <= c:
    return (a**2) + (c**2)
  elif c <= a and c <= b:
    return (a**2) + (b**2)
  else:
    return 0 
print(square_of_greaters(3,1,2))