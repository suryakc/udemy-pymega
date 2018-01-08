"""An interactive dictionary"""

import json
import requests

# Base url for our dictionary API.
PEARSON_API_URL_BASE = "http://api.pearson.com/v2/dictionaries/ldoce5/entries?headword="

def get_word_definition(word):
    """A function that fetches word meanings from web."""
    url = PEARSON_API_URL_BASE + word
    response = requests.get(url)
    return json.loads(response.text)


def dict_repl():
    """A function that continuously monitors the prompt for user input and
    and fetches word definitions"""
    while True:
        word = input("Please enter a word: ")
        if not word:
            print("Please enter a valid word")
            continue
        elif word == "exit" or word == "-1":
            break
        else:
            definition = get_word_definition(word)
            if definition is None or \
                definition["results"] is None or \
                len(definition["results"]) is 0:
                print("Word not found in dictionary...")
                continue

            print(definition["results"][0]["senses"][0]["definition"][0])


if __name__ == "__main__":
    dict_repl()
