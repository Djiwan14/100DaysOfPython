def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           if is_power(x):
            print(i)


print_factors(45)
