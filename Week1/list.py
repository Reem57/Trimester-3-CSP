song = []
# List with dictionary records placed in a list  
song.append({  
               "Artist": "NLE Choppa",
               "Year Released": "2022",  
               "Album": "Me vs. Me",  
               "Songs":["Shotta Flow 6","Push It","Jumpin", "Youngest to Do It", "Too Hot"]  
              })  

song.append({  
               "Artist": "DaBaby",  
               "Year Released": "2019",  
               "Album": "Baby on Baby",  
               "Songs":["Suge",	"Goin Baby","Pony","Taking It Out"]   
              })  

def print_data(n):
    print("Artist:", song[n]["Artist"])  # using comma puts space between values
    print("Album:", song[n]["Album"])
    print("Year Released:", song[n]["Year Released"])
    print("Songs: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(song[n]["Songs"]))  # join allows printing a string list with separator
    print()


def for_loop():
  print("For Loop: ")
  for n in range(len(song)):
        print_data(n)
    

def while_loop(n):
  print("While Loop: ")
  while n < len(song):
      print_data(n)
      n += 1
  return

def recursive_loop(n):
  print("Recursive Loop: ")
  if n < len(song):
      print_data(n)
      recursive_loop(n + 1)
  return # exit condition

def all_loops():
  for_loop()
  while_loop(0)
  recursive_loop(0)