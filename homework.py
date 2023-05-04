from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

print("All Pokemon named Pikachu")
results = pokemonColl.find({"name": "Pikachu"})
for p in results:
    print(p)

print("All Pokemon with an attack greater than 150")

results = pokemonColl.find({"attack": {"$gt":150}})
if results.explain()["executionStats"]["nReturned"] == 0:
    print("None Found")
else:
    for p in results:
        print(p)

print("All Pokemon with Overgrowth Ability")
results = pokemonColl.find({"abilities": {"$regex":"Overgrow"}})
for p in results:
    print(p)