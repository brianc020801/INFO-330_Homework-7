from pymongo import MongoClient
import sqlite3

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

db = sqlite3.connect("pokemon.sqlite")

def insertInto(): # Function to get neccessary data
    cur = db.cursor() # Open cursor
    cur.execute("SELECT p.name, p.pokedex_number, p.type1, p.type2, p.hp, p.attack, p.defense, p.speed, p.sp_attack, p.sp_defense, p.abilities FROM imported_pokemon_data AS p")
    pokemons = cur.fetchall()
    cur.close()
    db.close()
    for p in pokemons:
        if p[3] == '':
            types = "[" + p[2] + "]"
        else:
            types = "[" + p[2] + ", " + p[3] + "]"
        pokemon = {
            "name": p[0],
            "pokedex_number": int(p[1]),
            "types": types,
            "hp": p[4],
            "attack": p[5],
            "defense": p[6],
            "speed": p[7],
            "sp_attack": p[8],
            "sp_defense": p[9],
            "abilities": p[10]
        }
        pokemonColl.insert_one(pokemon)

insertInto()