import random


def fibonacci():
  print("How long do you want the list to be?")
  n = int(input().strip())
  num1 = random.randint(1,10)
  num2 = random.randint(1,10)
  print("number 1: " + str(num1))
  print("number 2: " + str(num2))
  total = num1
  for i in range(n):
    total = num1 + num2
    num1 = num2
    num2 = total
    print(total, end=", ")
  print("")

def fibonacciInput():
  print("How long do you want the list to be?")
  n = int(input().strip())
  print("Input number 1: ")
  num1 = int(input().strip())
  print("Input number 2: ")
  num2 = int(input().strip())
  total = num1
  for i in range(n):
    total = num1 + num2
    num1 = num2
    num2 = total
    print(total, end=", ")
  print("")
