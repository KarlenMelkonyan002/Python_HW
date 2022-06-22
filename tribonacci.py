"""This one is recursive"""
def f(n):
  if n < 3:
    return n
  return  f(n - 1) + f(n - 2) + f(n - 3)
print(f(4))

"""This one is iterative"""
def f1(n):
  a, b, c = 0, 1, 2
  while(n > 0):
    sum = a+b+c  
    a, b, c = b, c, sum
    n -= 1
  return a 
print(f1(5))

"""This one is tail recursion"""
def f3(n, sum, a = 0 , b = 1 , c = 2):
  if n < 3: 
    return n
  return(n-1, sum == a+b+c , a == b, b == c, c == sum )
print(f(4)) 