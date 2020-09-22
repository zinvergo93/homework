# phonebook = {
#     "Eric": 5556656,
#     "Beth": 5554863,
#     "Terry": 5554232,
# }
# phonebook['Austin'] = [5553232]
# print(phonebook)
# ************************************

# phonebook = {
#     "Eric": 5556656,
#     "Beth": 5554863,
#     "Terry": 5554232,
# }

# phonebook['Terry'] = [5552222]
# print(phonebook)

# **************************************

# phonebook = {
#     "Eric": 5556656,
#     "Beth": 5554863,
#     "Terry": 5554232,
# }

# found_number = phonebook.get("Eric")
# print(found_number)

# ***************************************

# COMPLEX DICTIONARY PLAYGROUND
# ***************************************
users = [
   {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
]

# 1***********************
print(users[0]["name"])

# 2***********************
print(users[0]["email"])

# 3***********************
print(users[1]["address"]["street"])

# 4***********************
print(users[0]["address"]["geo"]["lat"])

# 5***********************
print(users[1]["company"]["name"])

# 6***********************
users[0]["address"]["city"] = "Lehi"
print(users[0]["address"]["city"])

# 7**********************
users[1]["company"].pop("catchPhrase")
print(users[1]["company"])

# 8********************** EXTRA CREDIT
for user in users:
  print(user["name"])