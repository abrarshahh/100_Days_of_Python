#tresure map
print("Here are the loactions where you can put your Treasure at.")
print("🗺️ 🗺️ 🗺️ \n🗺️ 🗺️ 🗺️ \n🗺️ 🗺️ 🗺️")
row1 = ["🗺️","🗺️","🗺️"]
row2 = ["🗺️","🗺️","🗺️"]
row3 = ["🗺️","🗺️","🗺️"]

map = row1 + row2 + row3

position = input("Where do you want to put the treasure? \n")

if position == "11":
  map[0] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "12" :
  map[1] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "13" :
  map[2] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "21" :
  map[3] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "22" :
  map[4] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "23" :
  map[5] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "31" :
  map[6] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "32" :
  map[7] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")
elif position == "33" :
  map[8] = "X"
  print(f"{map[:3]} \n{map[3:6]} \n{map[6:]}")

else :
  print("Invalid Position.")