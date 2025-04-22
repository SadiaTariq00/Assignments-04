print ("01_add_many_number \n")

def add_num(numbers)->int:
  total_num: int = 0
  for i in numbers:
    total_num += i
  return total_num

def main():
  numbers:list[int] = [1,2,3,4,5]
  sum: int = add_num(numbers)
  print (sum)

if __name__ == '__main__':
  main()