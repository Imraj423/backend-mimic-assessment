#!/usr/bin/ python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next word.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

# import random
# import sys


# def mimic_dict(filename):
#     word_dict = {} # create an empty dict
#     alice = open(filename, 'r') # assign value of open file for read-only, to alice
#     text = alice.read() # text is open file and read text in file
#   #  alice.close() # close opened file that is alice
#     words = text.split() # split words in alice.txt
#     prev_word = ''
#     for word in words: #map words
#         if prev_word not in word_dict: # if previous word is not in mimic dict 
#             word_dict[prev_word] = [word] #then previous word in mimic is word thats been mapped
#         else:
#             word_dict[prev_word].append(word) #else if it is in mimicdict then add word to prev word
#         prev_word = word #so it goes word by word
#     return word_dict

#     raise NotImplementedError("Get to Work!")


# def print_mimic(mimic_dict, word):
#     """Given mimic dict and start word, prints 200 random words:
#         - Start with '' (empty string) as a seed word.
#         - Print the seed word
#         - Lookup this word in your mimic_dict and get it's value list
#         - Randomly select a new seed word from this word list
#         - Repeat this process 200 times
#     """
#     # +++your code here+++

#     for unused_word in range(200):
#         print(word)
#     next_word = mimic_dict.get(word)          # Returns None if not found
#     if not next_word:
#       next_word = mimic_dict['']  # Fallback to '' if not found
#     word = random.choice(nexts)
#     raise NotImplementedError("Get to Work!")


# # Provided main(), calls mimic_dict() and mimic()
# def main():
#     if len(sys.argv) != 2:
#         print 'usage: python mimic.py file-to-read'
#         sys.exit(1)

#     d = mimic_dict(sys.argv[0])
#     print_mimic(d, '')


# if __name__ == '__main__':
#     main()
import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  # LAB(begin solution)
  mimic_dict = {}
  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = text.split()
  prev = ''
  for word in words:
    if not prev in mimic_dict:
      mimic_dict[prev] = [word]
    else:
      mimic_dict[prev].append(word)
    # Could write as: mimic_dict[prev] = mimic_dict.get(prev, []) + [word]
    # It's one line, but not totally satisfying.
    prev = word
  return mimic_dict
  # LAB(replace solution)
  # return
  # LAB(end solution)


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  # LAB(begin solution)
  for unused_i in range(200):
    print word,
    nexts = mimic_dict.get(word)          # Returns None if not found
    if not nexts:
      nexts = mimic_dict['']  # Fallback to '' if not found
    word = random.choice(nexts)
  # The 'unused_' prefix turns off the lint warning about the unused variable.
  # LAB(replace solution)
  # return
  # LAB(end solution)


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()