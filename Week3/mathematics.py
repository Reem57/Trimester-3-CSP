import random

def createTask():
  a = int(input("Enter a number "))
  myList = []
  while a != 1:
    if a%2 ==0:
      a= a/2
      myList.append(int(a))
    else:
      a = 3 * a + 1
      myList.append(int(a))
  print(*myList)

def logic(a):
  for i in range (1, a + 1):
    myList = []
    while i != 1:
      if i%2 ==0:
        i= i/2
        myList.append(int(i))
      else:
        i = 3 * i + 1
        myList.append(int(i))
    print(len(myList), end=" ")

def inputLogic():
  logic(int(input("how many times do you want the function to run? ")))

def randomLogic():
  randomValue = random.randint(2,100)
  print("The function is going to run " + str(randomValue) + " times")
  logic(randomValue)