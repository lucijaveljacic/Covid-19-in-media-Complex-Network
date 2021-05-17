import pandas as pd
from datetime import datetime
from collections import Counter
from collections import defaultdict
import codecs
from collections import OrderedDict
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.pyplot import draw
from tabulate import tabulate
from statistics import mean
from nltk.corpus import stopwords


#BEZ STOPWORDS
# Get nltk stopword list into a set.
stop = set(stopwords.words('stopwords.txt'))

# Open and read in a text file.
file = open('prva.txt', encoding='utf-8-sig')
line = file.read()
words = line.split()

# stopwords found counter.
sw_found=0

# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in words:
    if not check_word.lower() in stop:
        # Not found on stopword list, so append.
        appendFile = open('prva_bezs.txt', 'a', encoding='utf-8-sig')
        appendFile.write(" " +check_word)
        appendFile.close()
    else:
        # It's on the stopword list
        sw_found +=1





# Get nltk stopword list into a set.
stop = set(stopwords.words('stopwords.txt'))

# Open and read in a text file.
file = open('druga.txt', encoding='utf-8-sig')
line = file.read()
words = line.split()

# stopwords found counter.
sw_found=0

# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in words:
    if not check_word.lower() in stop:
        # Not found on stopword list, so append.
        appendFile = open('druga_bezs.txt', 'a', encoding='utf-8-sig')
        appendFile.write(" " +check_word)
        appendFile.close()
    else:
        # It's on the stopword list
        sw_found +=1





# Get nltk stopword list into a set.
stop = set(stopwords.words('stopwords.txt'))

# Open and read in a text file.
file = open('treca.txt', encoding='utf-8-sig')
line = file.read()
words = line.split()

# stopwords found counter.
sw_found=0

# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in words:
    if not check_word.lower() in stop:
        # Not found on stopword list, so append.
        appendFile = open('treca_bezs.txt', 'a', encoding='utf-8-sig')
        appendFile.write(" " +check_word)
        appendFile.close()
    else:
        # It's on the stopword list
        sw_found +=1





# Get nltk stopword list into a set.
stop = set(stopwords.words('stopwords.txt'))

# Open and read in a text file.
file = open('cetvrta.txt', encoding='utf-8-sig')
line = file.read()
words = line.split()

# stopwords found counter.
sw_found=0

# If each word checked is not in stopwords list,
# then append word to a new text file.
for check_word in words:
    if not check_word.lower() in stop:
        # Not found on stopword list, so append.
        appendFile = open('cetvrta_bezs.txt', 'a', encoding='utf-8-sig')
        appendFile.write(" " +check_word)
        appendFile.close()
    else:
        # It's on the stopword list
        sw_found +=1