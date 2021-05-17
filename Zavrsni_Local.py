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


print('Analiza na lokalnoj razini')


#PRVA SKUPINA
print('\n1. Skupina: svi članci nastali u periodu 1.1.2020.-24.2.2020.')

file = open('prva_bezs.txt', 'r', encoding='utf-8-sig')
prvas = file.read()
#print(prvas)
prvas = prvas.replace('. ','')
prvas = prvas.replace('•','')
prvas = prvas.replace(':','')
prvas = prvas.replace('(','')
prvas = prvas.replace(')','')
prvas = prvas.replace('-','')
prvas = prvas.replace('/','')
#prva = prvas.split(',')
print(type(prvas))
#class str treba

dic = defaultdict(int)
prva_s = prvas.split()
for i in range(0, len(prva_s)-1):
    dic[str(prva_s[i]) + ' ' + str(prva_s[i+1])] += 1
prva_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    prva_sorted.append(("{} {}".format(w, dic[w])))
#print(prva_sorted)

with open('prva_mreza_bezs.txt', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)

with open('prva_mreza_bezs.edges', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)



g = nx.read_edgelist("prva_mreza_bezs.txt", create_using=nx.DiGraph(), data=(('weight', int),))
#print(g.edges())

#mjere centralnosti - degree
dc = nx.degree_centrality(g)
#print(dc)
dc = dict(sorted(dc.items(), key=lambda item: item[1]))
#print(dc)
degree = []
print('\nTop 10 centralnih čvorova prema degree: ')
for x in list(reversed(list(dc)))[0:10]:
    print("{}: {} ".format(x,  dc[x]))
    degree.append(("key {}, value {} ".format(x,  dc[x])))


#mjere centralnosti - betweenness
bet = nx.betweenness_centrality(g)
#print(bet)
bet = dict(sorted(bet.items(), key=lambda item: item[1]))
#print(bet)
betw = []
betww = []
print('\nTop 10 centralnih čvorova prema betweenness: ')
for x in list(reversed(list(bet)))[0:10]:
    print("{}: {} ".format(x,  bet[x]))
    betw.append(("{}, {} ".format(x,  bet[x])))
    betww.append(("{}".format(bet[x])))

for i in range(0, len(betww)):
    betww[i] = float(betww[i])
print(betww)



#DRUGA SKUPINA
print('\n2. Skupina: svi članci nastali u periodu 25.2.2020.-13.3.2020.')

file = open('druga_bezs.txt', 'r', encoding='utf-8-sig')
prvas = file.read()
#print(prvas)
prvas = prvas.replace('. ','')
prvas = prvas.replace('•','')
prvas = prvas.replace(':','')
prvas = prvas.replace('(','')
prvas = prvas.replace(')','')
prvas = prvas.replace('-','')
prvas = prvas.replace('/','')
#prva = prvas.split(',')
#print(type(prvas))
#class str treba

dic = defaultdict(int)
prva_s = prvas.split()
for i in range(0, len(prva_s)-1):
    dic[str(prva_s[i]) + ' ' + str(prva_s[i+1])] += 1
prva_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    prva_sorted.append(("{} {}".format(w, dic[w])))
#print(prva_sorted)

with open('druga_mreza_bezs.txt', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)

with open('druga_mreza_bezs.edges', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)


g = nx.read_edgelist("druga_mreza_bezs.edges", create_using=nx.DiGraph(), data=(('weight', int),))
#print(g.edges())

#mjere centralnosti - degree
dc = nx.degree_centrality(g)
#print(dc)
dc = dict(sorted(dc.items(), key=lambda item: item[1]))
#print(dc)
degree = []
print('\nTop 10 centralnih čvorova prema degree: ')
for x in list(reversed(list(dc)))[0:10]:
    print("{}: {} ".format(x,  dc[x]))
    degree.append(("key {}, value {} ".format(x,  dc[x])))



#mjere centralnosti - betweenness
bet = nx.betweenness_centrality(g)
#print(bet)
bet = dict(sorted(bet.items(), key=lambda item: item[1]))
#print(bet)
betw = []
betww = []
print('\nTop 10 centralnih čvorova prema betweenness: ')
for x in list(reversed(list(bet)))[0:10]:
    print("{}: {} ".format(x,  bet[x]))
    betw.append(("{}, {} ".format(x,  bet[x])))
    betww.append(("{}".format(bet[x])))

for i in range(0, len(betww)):
    betww[i] = float(betww[i])
print(betww)




#TRECA SKUPINA
print('\n3. Skupina: svi članci nastali u periodu 14.3.2020.-11.5.2020.')

file = open('treca_bezs.txt', 'r', encoding='utf-8-sig')
prvas = file.read()
#print(prvas)
prvas = prvas.replace('. ','')
prvas = prvas.replace('•','')
prvas = prvas.replace(':','')
prvas = prvas.replace('(','')
prvas = prvas.replace(')','')
prvas = prvas.replace('-','')
prvas = prvas.replace('/','')
#prva = prvas.split(',')
#print(type(prvas))
#class str treba

dic = defaultdict(int)
prva_s = prvas.split()
for i in range(0, len(prva_s)-1):
    dic[str(prva_s[i]) + ' ' + str(prva_s[i+1])] += 1
prva_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    prva_sorted.append(("{} {}".format(w, dic[w])))
#print(prva_sorted)

with open('treca_mreza_bezs.txt', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)

with open('treca_mreza_bezs.edges', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)

g = nx.read_edgelist("treca_mreza_bezs.edges", create_using=nx.DiGraph(), data=(('weight', int),))
#print(g.edges())

#mjere centralnosti - degree
dc = nx.degree_centrality(g)
#print(dc)
dc = dict(sorted(dc.items(), key=lambda item: item[1]))
#print(dc)
degree = []
print('\nTop 10 centralnih čvorova prema degree: ')
for x in list(reversed(list(dc)))[0:10]:
    print("{}: {} ".format(x,  dc[x]))
    degree.append(("key {}, value {} ".format(x,  dc[x])))


#mjere centralnosti - betweenness
bet = nx.betweenness_centrality(g)
#print(bet)
bet = dict(sorted(bet.items(), key=lambda item: item[1]))
#print(bet)
betw = []
betww = []
print('\nTop 10 centralnih čvorova prema betweenness: ')
for x in list(reversed(list(bet)))[0:10]:
    print("{}: {} ".format(x,  bet[x]))
    betw.append(("{}, {} ".format(x,  bet[x])))
    betww.append(("{}".format(bet[x])))

for i in range(0, len(betww)):
    betww[i] = float(betww[i])
print(betww)




#CETVRTA SKUPINA
print('\n4. Skupina: svi članci nastali u periodu 12.5.2020.-25.8.2020.')

file = open('cetvrta_bezs.txt', 'r', encoding='utf-8-sig')
prvas = file.read()
#print(prvas)
prvas = prvas.replace('. ','')
prvas = prvas.replace('•','')
prvas = prvas.replace(':','')
prvas = prvas.replace('(','')
prvas = prvas.replace(')','')
prvas = prvas.replace('-','')
prvas = prvas.replace('/','')
#prva = prvas.split(',')
#print(type(prvas))
#class str treba

dic = defaultdict(int)
prva_s = prvas.split()
for i in range(0, len(prva_s)-1):
    dic[str(prva_s[i]) + ' ' + str(prva_s[i+1])] += 1
prva_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    prva_sorted.append(("{} {}".format(w, dic[w])))
#print(prva_sorted)

with open('cetvrta_mreza_bezs.txt', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)

with open('cetvrta_mreza_bezs.edges', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)





g = nx.read_edgelist("cetvrta_mreza_bezs.edges", create_using=nx.DiGraph(), data=(('weight', int),))
#print(g.edges())

#mjere centralnosti - degree
dc = nx.degree_centrality(g)
#print(dc)
dc = dict(sorted(dc.items(), key=lambda item: item[1]))
#print(dc)
degree = []
print('\nTop 10 centralnih čvorova prema degree: ')
for x in list(reversed(list(dc)))[0:10]:
    print("{}: {} ".format(x,  dc[x]))
    degree.append(("key {}, value {} ".format(x,  dc[x])))


#mjere centralnosti - betweenness
bet = nx.betweenness_centrality(g)
#print(bet)
bet = dict(sorted(bet.items(), key=lambda item: item[1]))
#print(bet)
betw = []
betww = []
print('\nTop 10 centralnih čvorova prema betweenness: ')
for x in list(reversed(list(bet)))[0:10]:
    print("{}: {} ".format(x,  bet[x]))
    betw.append(("{}, {} ".format(x,  bet[x])))
    betww.append(("{}".format(bet[x])))

for i in range(0, len(betww)):
    betww[i] = float(betww[i])
print(betww)






