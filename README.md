# INFO330: Exploring Document Databases
A homework assignment for my INFO 330 course

## Background

Professor Oak had another problem.

(Prof Oak pic)

He called his new favorite Pokemon trainer and part-time IT support, Misty.

(Misty pic)

"Misty! I'm so glad I found you. Are you busy right now?"

Misty looked at the pool next to her, filled with hungry water Pokemon, and knew that they were going to have to go hungry for a bit longer. "No, Professor, what can I do for you?"

"After you did that great work normalizing the database, I started hearing some stories from the other Professors about a different way of storing the Pokemon data that might make it easier to do my research."

Misty frowned. "Did something happen to the existing database?" She glared at one of the Squirtles who "accidentally" blasted her iPad with a Water Gun attack the other day.

(Squirtle pic--Squirtle does not look embarrassed)

"No, no, it's great, it's just that the other Professors and I were talking and comparing data, and we found it would be easier to do so if we had a JSON version of each Pokemon that we could pass around to each other."

"Well, Professor, I guess, but I--"

"That's great Misty! Thank you!"

Misty sighed.

## Homework

In this directory is the CSV file and a version of the Pokemon normalized database. (We can assume they hold the same data--if you find any discrepancies, please let me know!) Your job is to import this data into a document database, such as MongoDB or Couchbase. (MongoDB is more popular, Couchbase has some features Mongo lacks; you are free to use either one.) You can either use features of the tool to do the import, or write Java or Python code to do it.

Regardless of which one you use, once the database is complete, store the data files for the database in this repository, and/or the code you used to import from the CSV or the SQLite database. Additionally, you must "export" the data from the new database in a JSON format, and store that JSON file in this repository as well.

## Rubric

* You have a JSON file that holds Pokemon; please call it `pokemon.json`. (1pt)
* This JSON file holds 801 Pokemon and their data, each in their own JSON entry. (2pts)
* Each JSON entry has all the data from the corresponding row in the CSV, but arranged hierarchically, per Pokemon. (1pt)
* Show a query against the database you used (either Mongo or Couchbase) that returns a single Pokemon's data (1 pt)

For the latter query, either show running it at the command-line, or take a screen shot of using a GUI tool to run the query (whichever is easier for you to use with the database in question--MongoDB has a command-line tool that ships with it, for example, but there are some GUI tools out that know how to query a MongoDB instance).

## Extra credit

* include a new attribute for each Pokemon, "image", that contains an HTTP URL to a pic of the Pokemon. Populate this for "Bulbasaur", "Ivysaur", and "Venusaur". (2 pts)
* use the facilities of the document database you choose (Mongo or Couchbase) to answer the following questions (1 pt each):
    * How many Pokemon have just one type?
    * How many Pokemon are "Poison" type as either their first or second type?
    * How many Pokemon have an attack that no other Pokemon has?


## Tips

JSON is a hierarchical format, where we start with a common root (either an object or an array) and has name-value pair children beneath it. JSON also does not look to normalize the data--instead, the heart of its model is to take a more "document" approach, where everything about the entity is captured in one place, duplicated if necessary. (It has much in common with CSV that way.) So a reasonable "first pass" at a JSON-based schema for each entry could look like:

```
{
    'name': 'Bulbasaur',
    'types': ['grass', 'poison'],
    'generation': 1
}
```

You are free to use whatever schema makes sense to you, so if you found it easier to arrange them by generation, you could do something like the following:

```
{
    'generations': [
        [
            {
                'name': 'Bulbasaur',
                'types': ['grass', 'poison'],
                'generation': 1
            }
        ]
    ]
}
```

... where `generations` is an array, and each element in that array is the array of Pokemon that came out with that generation. It's entirely up to you.
