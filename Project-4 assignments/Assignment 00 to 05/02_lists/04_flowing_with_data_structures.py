print ("04_flowing_with_data_structures \n")

def three_copies(mylist,data):
  for i in range(3):
    mylist.append(data)

def main():
  mymessage = input("Enter a Message: ")
  mylist=[]
  print("Before list is: ", mylist)
  three_copies(mylist, mymessage)
  print("After list is: ", mylist)

if __name__ == '__main__':
   main()
