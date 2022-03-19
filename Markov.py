
# Markov chains are a mathematical tool used to generate output that mimics a given sample. 
# For the Markov chains algorithm to work, it first needs a sample as big as possible of the 
# kind of material it will generate. The program chunks this initial input into small items,
# in this case, words. For each item, it browses the sample and looks at which item immediately
# follows. Taking the number of items into account, the program computes a probability 
# for each item to be the one that follows a given item.
# This process creates a statistical 
# model of the input. It assumes that the input is representative enough 
# as a sample to give an idea of the general rules followed by the material.
# Once the statistics are computed, the algorithm starts with a random item 
# from the list and picks the item that succeeds based on the statistical 
# model of the current item 
# and a randomly computed probability. It repeats the process with each subsequent item. 

#1)load the text
with open('frank.txt') as f:
    text = f.read()
    #print(text)
#2) text preprocessing
from nltk.tokenize import word_tokenize
from collections import Counter

text=text.lower()
my_text=[i for i in word_tokenize(text) if i.isalpha() and i not in [".",",",";","!","?"]]
#print((my_text[:5]))
#print(my_text.index("ever-moving"))
single_word=set(my_text)
print(len(single_word))
word_freq=Counter(my_text)
#print(word_freq)

import random as r
def find_index(l,w):
    indices = [i+1 for i, x in enumerate(l) if x == w]
    return indices
mapping={}
for i in single_word: 
  indice=find_index(my_text,i)
  mapping[i]=indice

def markov(i,x,s,t=i):
    if x>=0:
     next_w=s[r.choice(mapping.get(i))]
     t+=" "+(next_w)
     markov(next_w,x-1,s,t)
    else:
        print(t)
initial_w=input("what's the first word? ")
nbr_lines=int(input("how many lines?  "))
markov(initial_w,nbr_lines,my_text,initial_w)


# import json
# # Serializing json 
# json_object = json.dumps(mapping, indent = 4)
  
# # Writing to sample.json
# with open("markov_chain.json", "w") as outfile:
#     outfile.write(json_object)