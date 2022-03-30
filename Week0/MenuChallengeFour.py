import time
import os


def printShip():
    distance = int(input("How far should the ship go? "))
    for i in range(int(distance)):
        print("  "*i,"    |\ ")
        print("  "*i,"    |/ ")
        print("  "*i,"\__ |__/ ")
        print("  "*i," \____/ ")
        os.system("cls")
        print("\u001b[34m {dashes} \u001b[37m".format(dashes = "--"*distance))

        time.sleep(0.006)
if __name__ == "__main__":
    printShip()
