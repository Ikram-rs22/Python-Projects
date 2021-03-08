import json
from difflib import get_close_matches
data = json.load(open("dictionary.json"))

def Seek(word):
             word = word.lower()
             if(word in data):
                 return data[word]
             elif(word.title() in data):
                 return data[word.title()]
             elif(word.upper() in data):
                 return data[word.upper()]
             elif(len(get_close_matches(word,data.keys())[0])>0):
                 print("Did you mean %s by this?" %get_close_matches(word,data.keys())[0])
                 decide = input("Type yes or no: ")
                 if(decide=="yes"):
                     print(data[get_close_matches(word,data.keys())[0]])
                 else:
                     print("We cannot find what you want")
             else:
                 print("This word does not exist")

word = input("Search the word you want: ")
output = Seek(word)
if(type(output)==list):
    for item in output:
        print(item)
else:
    print(output)