# Write a program to determine if a number, given on the command line, is prime.

user_input = int(input("Enter a number to determine if it's a Prime: \n> "))

def is_prime(x):
  if x > 1:
    for num in range(2, x):
      if(x % num == 0):
        return False
    return True
  return False

result = is_prime(user_input)
print(result)