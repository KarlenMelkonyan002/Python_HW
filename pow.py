'''Everything works when base > 0 !!!!'''
def pow(base, exp):
  res = 1
  count = 0
  while count < exp:
		 res = res * base
		 count = count + 1
  return res

def all_pow(base, exp):
  if(base == 0 and exp < 0):
    return None
  elif (base > 0 and exp > 0):
    return pow(base,exp)
  elif (base > 0 and exp < 0 ):
    return 1/pow(base,exp)
  else:
    return 1

print(all_pow(5,3))
  
   