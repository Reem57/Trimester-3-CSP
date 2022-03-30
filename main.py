from menu import presentMenu
from menu import mainMenu

if __name__ == "__main__":
  while True:
    presentMenu(mainMenu)
    halt = input("Do you want to continue (y/n)? ")
    if halt.lower() == "n":
      break  