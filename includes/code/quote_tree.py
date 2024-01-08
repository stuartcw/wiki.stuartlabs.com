#!/usr/local/bin/python3
#md# quote_tree.py
#mdA program to read a collection of quotes from a csv file and provide a CGI based JSON API to retrieve random quotes generated from the frequency data of the words and following words in the input quotes.
import os

#md### Import the required libraries.
import string
import csv
import json
import random
import pprint
from collections import defaultdict

MAX_WORD_COUNT=10

#md Set the location file holding the generated quote data.
CURRENT_FOLDER=os.getcwd()
QUOTE_FILE=CURRENT_FOLDER+"/quotes.json"

def process_quotes():
    #md **This function reads all the quotes afresh and returns a node graph structure eroniously called tree in a dictionary comprising of a key labeling a node and a value containing a list of the lables that a node connects to. No attempt is made remove duplicates in the lable list as this is used later to weight the chance of being selected when the random quote is created from this data.**

    #md Collect the authors of the quotes in a set of unique author names.
    authors=set()

    #md Read in the quotes from the CSV file. #TODO move this hardcoded path to a constant.
    quotes = csv.reader(open(CURRENT_FOLDER+"/quotes.csv"))

    #md Skip over the header which is the first line of the CSV file.
    next(quotes)

    #md `tree` is the main data structure in the program.
    tree = defaultdict(list)

    #md Iterate throught the quotes. i is the row count, row is the a tuple.
    for i,row in enumerate(quotes):

        #md Extract the author and quote from the row data.
        author,quote = row

        #md Add this author to set of authors.
        authors.add(author)

        #md We now read the words of the quote one by one. Initially there is no previous word.
        previous_word=None
        #md split the `quote` into `parts` separated by spaces.
        parts=quote.split()

        #md For each word in the quote, append it to the previous words list of following words.
        for word in parts:
            if previous_word:
                tree[previous_word].append(word)
            previous_word=word

    #md Assume that words which start a quote start with a capital letter. #TODO fix this.
    start_words=[word for word in tree.keys() if word[0].upper()==word[0] ]
    #md This looks like it is not used.
    other_words=[word for word in tree.keys() if word[0].upper()!=word[0] ]

    #md Convert the set into a list as JSON doesn't no how to encode sets.
    authors=list(authors)

    return tree, start_words, other_words, authors

def get_quote(tree, start_words, other_words, authors):
    #md**A function to return a randomly generated psuedo quote based on the quote data.**

    #md This is the return value.
    sentence=[]
    #md Choose a random word to start the sentence.
    w=random.choice(start_words)
    sentence.append(w)

    #md Set a limit of 100 word long sentences. This is an artibary choice but there is no guarantee that the loop will end without it.
    for i in range(0,100):
        #md This `try` is probably not needed anymore but was useful in debugging. #TODO fix
        try:
            #If the word is not a node then quit. #TODO is this needed now?
            if not w in tree: 
                break

            #md Start with unpopulated word list selection.
            wordlist=[] 

            # If we have reached the expected maximum length for a sentence then limit the word selection to only those which end in a full stop. This can be an empty list.  #TODO Check the word ending chars.
            if i>MAX_WORD_COUNT:
                wordlist=[ w for w in tree[w] if w[-1] =="." ] 
            #If there are no ending words defined then allow a full selection of following words.
            if not len(wordlist):
                wordlist=tree[w]

            #md Choose a random word from the word list.
            w=random.choice(wordlist)
            #md Add it to the sentence.
            sentence.append(w)
        except IndexError:
            print(w)
            print(tree)
            break

    #md **Return the sentence followed by 2 newlines and a random author.**
    return " ".join(sentence)+"\n\n" + random.choice(authors)

#md This could be in a separate file.
#md import the CGI libraries, just for debugging.
import cgi
import cgitb
cgitb.enable()

print("Content-Type: application/json; charset=utf-8\n\n")

#md Assume that the JSON quote file has been generated and load it.
try:
    data=json.load(open(QUOTE_FILE))
#md If loading the JSON quote data fails then create it and save it, loading it into `data`. This means that the first hit may take a while to complete.
except FileNotFoundError:
    tree, start_words, other_words, authors=process_quotes()
    data={"tree":tree, "start_words":start_words, "other_words":other_words, "authors":authors}
    json.dump(data,open(QUOTE_FILE, "w"),indent=4)

#md This holds the return data.
markov_quotes=[]
#md Assume the requestor wants 10 quotes.
for f in range(0,10):
    markov_quotes.append(get_quote(data["tree"], data["start_words"], data["other_words"],data["authors"]))
#md return them via HTTP JSON response.
print(json.dumps({"quotes":markov_quotes},indent=4))
