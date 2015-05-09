__author__ = 'Emma Grasmeder'
"@emma_gras" # Twitter
# For the Mother-Daughter Hackathon (30 minutes)
# Note: Written for Python 3

## Basic Data Structures:
#examples of integers:
1
2
33
-99999

# examples of strings:
"cat"
"house"
"36"
"[ ]"
"one"

# examples of variables
x = 13
var1 = "these few w0rds"

# examples of lists:
word_list = ["cat", "dog", "house"]
int_list = [1, 2, 3, 4]
list_of_lists = [[1, 2, 3],
                 ["a", "b", "c"],
                 []]

# examples of dictionaries:
word_dictionary = {"housecat": "a small mammal that says 'meow' ",
                   "dog": "a human's best friend",
                   "house": "a common habitat for humans to dwell"}
int_to_string_dict = {1: ["one", "1"],
                      2: ["two", "2"],
                      303: ["three hundred three", "303"]}


## A Minimum Viable Cook Book!
# Dishes are stored in the format: ["dish name",
#                                   "ingredient 1",..."ingredient n"]
#                                   for all n in the required ingredients
boiled_egg = ["boiled egg","egg"]
scrambled_egg = ["scrambled egg", "egg"]
french_bread = ["french bread", "flour", "yeast", "salt", "water"]

recipes = [boiled_egg, scrambled_egg, french_bread]
what_we_have = []  # this is an empty list that will be filled with user input
while True:
    response = str(input("enter ingredients you have, then type 'done' when finished: "))
    if response != "done":
        what_we_have.append(response)
    else:
        break
for r in recipes:  # here we're iterating through all the recipes
    # The first item in r is the name of the dish, so ignore it
    ingredients = r[1:]  # we ignore the first item by slicing
    if set(ingredients).issubset(set(what_we_have)):  # see note below
        print("You can cook {}!".format(r[0]))

    # note about "set(a).issubset(set(b))":
    # Think about venn diagrams when thinking about subsets.
    #   [1,2,3] is a subset of [5,4,3,2,1] because every item in
    #   the list [1,2,3] is also in [5,4,3,2,1].
    # If we have 5 products and the recipe only requires 3 out of that
    #   the 5, we can be certain we can make the recipe.
