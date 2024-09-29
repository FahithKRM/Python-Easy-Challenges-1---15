def SumList():
  number_list = [34, 66, 125, 67, 817]
  total = 0
  for i in range(len(number_list)):
     total += number_list[i]

  return total

print("Total of number list = ", SumList())
