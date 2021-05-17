import pandas as pd
from datetime import datetime
from collections import defaultdict


df = pd.read_csv("podaci.csv", encoding='utf-8-sig')
#print(df)
df["Text"] = df["Naslov"] + ' ' + df["Tekst"]
pd.options.display.max_colwidth = None
#print(df.head())
#print(df)

df['Datum'] = pd.to_datetime(df['Datum'])



#1. Skupina: svi članci nastali u periodu 1.1.2020.-24.2.2020.
mask = (df['Datum'] >= '2020-1-1') & (df['Datum'] <= '2020-2-24')
df1 = df.loc[mask]
df1 = df1['Text']
df1 = df1.str.replace('\W+', ' ', True)

prva = []
for row in df1:
    prva.extend(row)
#print(prva)
prva = ''.join([str(elem) for elem in prva])
#print(prva)
prva = prva.lower()
with open('prva.txt', 'w', encoding='utf-8-sig') as f:
    f.write(prva)
#print(type(prva))

#2. Skupina: svi članci nastali u periodu 25.2.2020.-13.3.2020.
mask = (df['Datum'] >= '2020-2-25') & (df['Datum'] <= '2020-3-13')
df2 = df.loc[mask]
df2 = df2['Text']
df2 = df2.str.replace('\W', ' ', True)

druga = []
for row in df2:
    druga.extend(row)
#print(druga)
druga = ''.join([str(elem) for elem in druga])
#print(druga)
druga = druga.lower()
with open('druga.txt', 'w', encoding='utf-8-sig') as f:
    f.write(druga)

#3. Skupina: svi članci nastali u periodu 14.3.2020.-11.5.2020.
mask = (df['Datum'] >= '2020-3-14') & (df['Datum'] <= '2020-5-11')
df3 = df.loc[mask]
df3 = df3['Text']
df3 = df3.str.replace('\W', ' ', True)
#print(df3)

treca = ''.join([str(elem) for elem in df3])
#print(treca)
treca = treca.lower()
with open('treca.txt', 'w', encoding='utf-8-sig') as f:
    f.write(treca)

#4. Skupina: svi članci nastali u periodu 12.5.2020.-25.8.2020.
mask = (df['Datum'] >= '2020-5-12') & (df['Datum'] <= '2020-8-25')
df4 = df.loc[mask]
df4 = df4['Text']
df4 = df4.str.replace('\W', ' ', True)
cetvrta = []
for row in df4:
    cetvrta.extend(row)
#print(cetvrta)
cetvrta = ''.join([str(elem) for elem in cetvrta])
#print(cetvrta)
cetvrta = cetvrta.lower()
with open('cetvrta.txt', 'w', encoding='utf-8-sig') as f:
    f.write(cetvrta)










#2. ZADATAK

#1.
dic = defaultdict(int)
prva_s = prva.split()
for i in range(0, len(prva_s)-1):
    dic[str(prva_s[i]) + ' ' + str(prva_s[i+1])] += 1
prva_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    prva_sorted.append(("{} {}".format(w, dic[w])))
#print(prva_sorted)

with open('prva_mreza.txt', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)

with open('prva_mreza.edges', 'w', encoding='utf-8-sig') as f:
    for item in prva_sorted:
        f.write("%s\n" % item)

#2.
dic = defaultdict(int)
druga_s = druga.split()
for i in range(0, len(druga_s)-1):
    dic[str(druga_s[i]) + ' ' + str(druga_s[i+1])] += 1
druga_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    druga_sorted.append(("{} {}".format(w, dic[w])))
#print(druga_sorted)

with open('druga_mreza.txt', 'w', encoding='utf-8-sig') as f:
    for item in druga_sorted:
        f.write("%s\n" % item)

with open('druga_mreza.edges', 'w', encoding='utf-8-sig') as f:
    for item in druga_sorted:
        f.write("%s\n" % item)

#3.
dic = defaultdict(int)
treca_s = treca.split()
for i in range(0, len(treca_s)-1):
    dic[str(treca_s[i]) + ' ' + str(treca_s[i+1])] += 1
treca_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    treca_sorted.append(("{} {}".format(w, dic[w])))
#print(treca_sorted)

with open('treca_mreza.txt', 'w', encoding='utf-8-sig') as f:
    for item in treca_sorted:
        f.write("%s\n" % item)

with open('treca_mreza.edges', 'w', encoding='utf-8-sig') as f:
    for item in treca_sorted:
        f.write("%s\n" % item)

#4.
dic = defaultdict(int)
cetvrta_s = cetvrta.split()
for i in range(0, len(cetvrta_s)-1):
    dic[str(cetvrta_s[i]) + ' ' + str(cetvrta_s[i+1])] += 1
cetvrta_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    cetvrta_sorted.append(("{} {}".format(w, dic[w])))
#print(cetvrta_sorted)

with open('cetvrta_mreza.txt', 'w', encoding='utf-8-sig') as f:
    for item in cetvrta_sorted:
        f.write("%s\n" % item)

with open('cetvrta_mreza.edges', 'w', encoding='utf-8-sig') as f:
    for item in cetvrta_sorted:
        f.write("%s\n" % item)







#3. ZADATAK
#Članci nastali u periodu 1.1.2020.-25.8.2020.
mask = (df['Datum'] >= '2020-1-1') & (df['Datum'] <= '2020-8-25')
df5 = df.loc[mask]
df5 = df5['Text']
df5 = df5.str.replace('\W', ' ', True)
df5 = df5.str.replace('“', ' ', True)
df5 = df5.str.replace('-', ' ', True)
df5 = df5.str.replace('.', ' ', True)
df5 = df5.str.replace('–', ' ', True)
sve = ''.join([str(elem) for elem in df5])
sve = sve.lower()
with open('cijeli_tekst.txt', 'w', encoding='utf-8-sig') as f:
    f.write(sve)

dic = defaultdict(int)
sve_s = sve.split()
for i in range(0, len(sve_s)-1):
    dic[str(sve_s[i]) + ' ' + str(sve_s[i+1])] += 1
sve_sorted = []
for w in sorted(dic, key=dic.get, reverse=True):
    #print(w, dic[w])
    sve_sorted.append(("{} {}".format(w, dic[w])))

with open('cijela_mreza.txt', 'w', encoding='utf-8-sig') as f:
    for item in sve_sorted:
        f.write("%s\n" % item)

with open('cijela_mreza.edges', 'w', encoding='utf-8-sig') as f:
    for item in sve_sorted:
        f.write("%s\n" % item)
        
