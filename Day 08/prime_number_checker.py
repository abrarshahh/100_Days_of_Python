#prime number checker
def prime_check(number):
  is_prime = True
  
  for div in range(2,number):
    if number % div == 0:
      is_prime = False

  if is_prime:
    print(f"{number} is a prime number")

  else:
    print(f"{number} is not a prime number")
      

num = int(input("Enter a number:  "))
prime_check(number=num)