# INFO330: Exploring Document Databases
A homework assignment for my INFO 330 course, building around the Pokemon CSV file from [INFO330-CreatingRelations2](https://github.com/tedneward/INFO330-ExploringRelations2).

Feel free to [skip the story](#goals) if you wish.

## Background
Professor Oak was sitting at his computer when he was surprised to receive a call from Professor Birch. 

![](Images/Birch.jpeg)

*Professor Birch was always late to class*

"Birchie! How's the Hoenn region?"

"Quite pleasant, Samuel. How's Johto?"

They chatted pleasantly for a few minutes. Then Professor Oak said, "What can I do for you? Anything going on?"

"Well, as it turns out, I'm joining a startup--a company called Rocket Pokemon, they're sort of an outgrowth of the same folks that do mortgages and loans--and I could use your help."

![](Images/Rocket.jpeg)
![](Images/rocket-mortgage.png)

*Are they the same company? You decide for yourself.*

Professor Oak was confused. "I'm happy for you, Birchie, but why...?"

"Why call you? Because! I want your help! We want to start running some experiments where we put thousands of Pokemon into battles--"

![](Images/multi-pokemon-battle.jpeg)

Professor Oak gasped. "Birchie! You're talking Pokemon WAR?!?"

"No, no! No. We want to *simulate* those battles. We think it'll be useful for research."

"Oh!" Professor Oak was relieved. "Well, how can I help?"

Professor Birch smiled. "I was hoping you'd ask! You see, we need your Pokemon database to be in our database."

Professor Oak started to get a bad feeling in his stomach. "Well, I'm happy to share my SQL database with you..."

"No, I'm sorry Samuel, but we find that a SQL database can't handle the millions of simulations we're going to run. We were hoping you could port it into a document database...? If you could, maybe, put the data into MongoDB...?"

Suddenly Professor Oak wanted to see Team Rocket Corp in a familiar pose.

![](Images/blasting_off_again.jpeg)

## Goals
Using either the CSV file or the SQLite database provided (whichever you find easier to use), import the data into a MongoDB database and make sure it is usable from a Python program (which will simulate some pokemon battles). You may need to use the `mongosh` client to manipulate the imported documents to match the desired format.

### Details

First, fork this repository so it is a part of your own GitHub account. Then clone it to your local machine so you can work on it.

Next, [install MongoDB](https://www.mongodb.com/docs/manual/installation/) on your personal machine. (If you have technical difficulties doing that, you are free to explore using one of the free cloud MongoDB providers, but keep in mind that the TAs may not be able to help much if you run into issues.) Create a database called `pokemon`.

> **NOTE:** If your laptop is relatively recent, you can install Docker, which is a tool for hosting virtual environments; see http://www.docker.com . Once installed, a MongoDB container can be obtained by running `docker run --name mongodb -d -p 27017:27017 -v $(pwd)/data:/data/db mongodb/mongodb-community-server:latest` This will allow you to connect to the database via `mongosh`, and data will be stored in a "data" subdirectory underneath whatever the current directory is. (And if all of that is gobbledy-gook to you, it'll be much easier for you to download and install MongoDB on your laptop directly.)

Once MongoDB (the MongoDB server program is called `mongod`) is running, connect to it with `mongosh` to make sure you can connect to it. (If you are having difficulties, try running `mongod --config mongo.conf` from this directory; it will make use of the configuration file in this directory to hopefully make it easier to connect.)
You should see this:

```
~/Projects/UW/INFO330-ExploringDocDBs % mongosh
Current Mongosh Log ID:	644a0ee87ac72be6cf6689ee
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.1
Using MongoDB:		6.0.5
Using Mongosh:		1.8.1
```

... along with (potentially) a lot more information. At the end of all that, however, you should see something like this:

```
test>
```

This is the *MongoDB Shell prompt*, and it is similar in some ways to running `sqlite3` from the command prompt: It is an interactive shell that you can use to interact with a MongoDB program. You can tyoe `help()` to get a list of commands that the shell recognizes, or `db.help()` to get a list of methods on the top-level `db` object.

Once you know that MongoDB is up and running, you can dive into the bulk of the assignment.

### Collections

In your `pokemon` database, you will need to have a collection `pokemon_data`, which will contain instances of JSON/BSON documents that look roughly like the following:

```
{
    "_id": (some alphanumeric value),
    "name": "Bulbasaur",
    "pokedex_number": 1,
    "types": ["grass", "poison"],
    "hp": 45,
    "attack": 49,
    "defense": 59,
    "speed": 45,
    "sp_attack": 65,
    "sp_defense": 65
    "abilities": [
        "Chlorophyll", "Overgrow"
    ]
}
```

Notice that this is just the combat statistics of the Pokemon; Team Rocket doesn't care about any data except that which can be used in battles. Keep in mind, this is just one Pokemon; the collection will be an array of Pokemon in JSON format.

## Stories/Rubric

Create Python scripts that do the following:

* Write a query that returns all the Pokemon named "Pikachu". (1pt)
* Write a query that returns all the Pokemon with an attack greater than 150. (1pt)
* Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)

These can be either in their own `.py` files or all in one file, whichever you find easier. You may find it helpful to use the `Validate.py` script as an example. Run these on your machine, and capture the run in a video. Commit those video files to this repository.

Now it's time to run some battles; use Python to run the `Battle.py` script. If it runs into problems, it will print out an error message. Your job is to correct the database to match the script's expectations. (Do not change the Python code.)

* Python script can execute a battle between Pokemon. (2pts)

Again, run this file and capture the output as a video.

## Extra credit

* **Be your best Team Rocket. (2 pts)** Record a video of yourself saying, "Looks like Team Rocket is blasting off again....!" and submit it in this repository.

* **Improve the Battle.py script. (2 pts)** The algorithm in the Battle.py script is pretty lame. (Team Rocket is NOT known for its skills in evaluating Pokemon.) Improve it and commit the changes to this repository. Make sure to point out to your TA that you have improved it, so they can verify it and give you the extra point.
