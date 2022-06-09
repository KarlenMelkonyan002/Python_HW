def sum_of_range(a, b):
   sum = 0;
   while(b - a) >= 0:
    sum+=a
    a+=1
   return sum

def sum_of_range_inversed(a,b):
  sum=0
  while(a - b) >= 0:
   sum+=a
   a-=1
  return sum

def sum_of_range_better_version(a,b):
 if (b-a) < 0:
   return sum_of_range_inversed(a,b)
 return sum_of_range(a,b)
print(sum_of_range_better_version(-1,3))  
