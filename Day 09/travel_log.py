# travel log

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities_visited": ["Paris" , "Lille", "Dijon"],
  },

  {
    "country": "Germany",
    "visits": 5,
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  },
]

def add_new_place(country,visits,cities_visited):
  country = input("What country did you visit? ")
  visits = int(input("How many times have you been there"))
  cities_visited = input("What cities did you visit? ").split(", ")

  travel_log.append({"country": country, "visits": visits, "cities_visited": cities_visited})

add_new_place("country","visits","cities_visited")
print(travel_log)