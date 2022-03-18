
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
    print(text)
#2) text preprocessing
