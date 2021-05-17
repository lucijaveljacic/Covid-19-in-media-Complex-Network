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


g = nx.read_edgelist("cijela_mreza.edges", create_using=nx.DiGraph(), data=(('weight', int),))
#print(g.edges())
g2 = nx.read_weighted_edgelist("cijela_mreza.edges")


#GLOBALNE MJERE (usmjerena i težinska mreža)
print('\nAnaliza na globalnoj razini')
N = g.number_of_nodes()
print('N = ', N)

K = g.number_of_edges()
print('K = ', K)

PSM = K/N
print('Prosječan stupanj mreže: ', PSM)

GM = K/(N*(N-1))
print('Gustoća mreže: ', GM)

print('Je li graf jako povezan? ', nx.is_strongly_connected(g))
br_j_komp = nx.number_strongly_connected_components(g)
print('Broj jako povezanih komponenti: ', br_j_komp)
print('Je li graf slabo povezan? ', nx.is_weakly_connected(g))
br_sl_komp = nx.number_weakly_connected_components(g)
print('Broj slabo povezanih komponenti: ', br_sl_komp)

av_sh_pth_ln = nx.average_shortest_path_length(g)
print('Prosječna duljina najkraćeg puta iznosi:', av_sh_pth_ln)

diameter = nx.diameter(g2)
print('Dijametar mreže: ', diameter)

gl_koef_gr = nx.transitivity(g)
print('Globalni koeficijent grupiranja: ', gl_koef_gr)

gl_ass = nx.degree_pearson_correlation_coefficient(g)
print('Globalni koeficijent asortativnosti: ', gl_ass)


#Histogram distribucije stupnjeva
def plot_degree_dist(g):
    degrees = [g.degree(n) for n in g.nodes()]
    plt.hist(degrees)
    plt.xlabel('Stupanj')
    plt.ylabel('Broj čvorova')
    plt.title('Dijagram distribucije stupnjeva')
    plt.show()
plot_degree_dist(g)


