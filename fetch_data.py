import requests
playerID = input("Player ID(WITHOUT #): ")
response = requests.get(f"https://api.clashroyale.com/v1/players/%23{playerID}/upcomingchests", headers = {"Accept":"application/json", "authorization":f"Bearer API"}, params = {"limit":1})
#gets the players upcoming chest information
chests = response.json()["items"]
print(chests)  #takes in the information from the get request
getname = requests.get("https://api.clashroyale.com/v1/players/%238UUC8UL0", headers = {"Accept":"application/json", "authorization":"Bearer API"}, params = {"limit":1})
#gets the players name information
if response.status_code == 200 and getname.status_code == 200:
    if "name" in getname.json():            #finds the name of the player and prints the initial message
        print(f"{getname.json()["name"]}'s upcoming chests are:")
    count = 0
    for i in chests:            #prints upcoming chests in order
        count += 1
        print(f"{count}.",  i["name"])
else:
    print("Error: Player not found.")
intro = print(f"{getname.json()["name"]}'s upcoming chests are:")
chestwrite = print(f"{count}.",  i["name"])
info = "clash.json"
with open(info, "w", encoding="utf-8") as f:
   f.write(f"{getname.json()["name"]}'s upcoming chests are: ")
   f.write(F"{chests}")
print("Saved to clash.json")  