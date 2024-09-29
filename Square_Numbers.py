# code 01
def SquareNumbers(number):
  square_list = []
  for i in range(1, number+1):
    square_list[i-1] = i**2
  return square_list 


number = int(input("Enter the number : "))
print("Return the Square numbers 1-{number} :\n", SquareNumbes(number))


# code 02
"""def SquareNumbers(number):
  for i in range(1, number+1):
    print(f"Square of {i} = ", i**2)


number = int(input("Enter the number : "))
print("Return the Square numbers 1-{number} :")
SquareNumbes(number)"""


