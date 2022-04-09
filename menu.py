from Week0.MenuChallengeThree import printTree
from Week0.MenuChallengeFour import ship
from Week0.MenuChallengeTwo import print_matr
from Week0.MenuChallengeTwo import swap
from Week1.fibonacci import fibonacci
from Week1.fibonacci import fibonacciInput
from Week1.list import all_loops
from Week2.hack2 import dispfac
from Week2.hack2 import dispSeries
from Week2.hack3 import superfac
from Week3.mathematics import createTask
from Week3.mathematics import logic
from Week3.mathematics import inputLogic
from Week3.mathematics import randomLogic

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key}. {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()
        else:
            presentMenu(menu[choice]["exec"])
subMenu = {
    1: {"display":"Generate a random number",
        "exec":fibonacci,
        "type":"func"},
    2: {"display":"Input your own two numbers",
        "type":"func",
        "exec":fibonacciInput,}
}

drawing = {
  1: {"display":"Christmas Tree",
        "exec":printTree,
        "type":"func"},
    2: {"display":"Aardvark",
        "exec":ship,
        "type":"func"},
    3: {"display":"Keypad ",
        "exec":print_matr,
        "type":"func"}
}

createTaskMenu = {
  1: {"display":"Print List",
      "exec":createTask,
      "type":"func"},
  2: {"display":"Input Number to repeat",
    "exec": inputLogic,
    "type":"func"},
  3: {"display":"Generate a random number to repeat",
    "exec": randomLogic,
    "type":"func"}
}

math = {
  1: {"display":"Swap ",
      "exec":swap,
      "type":"func"},
  2: {"display":"Fibonacci",
    "exec": subMenu,
    "type":"submenu"},
  3: {"display":"Create Task Options",
    "exec": createTaskMenu,
    "type":"submenu"}
}
factorialMenu = {
  1: {
    "display": "Factorial calculator",
    "exec": dispfac,
    "type": "func"
  },
  2: {
    "display": "Factorial series",
    "exec": dispSeries,
    "type": "func"
  },
  3: {
    "display": "Superfactorial",
    "exec": superfac,
    "type": "func"
  }
}

mainMenu = {
    1: {"display":"Drawing",
        "exec":drawing,
        "type":"submenu"},
    2: {"display":"Math",
        "exec":math,
        "type":"submenu"},
    3: {"display":"Song Loops",
        "exec": all_loops,
        "type":"func"},
    4: {"display":"Factorial",
        "exec": factorialMenu,
        "type":"submenu"}
}