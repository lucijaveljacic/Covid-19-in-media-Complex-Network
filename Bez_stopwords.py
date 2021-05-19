from collections import Counter
from nltk.corpus import stopwords


#BEZ STOPWORDS
def stopw(x):
    # Get nltk stopword list into a set.
    stop = set(stopwords.words('stopwords.txt'))

    # Open and read in a text file.
    file = open(str(x)+'.txt', encoding='utf-8-sig')
    line = file.read()
    words = line.split()

    # stopwords found counter.
    sw_found=0

    # If each word checked is not in stopwords list,
    # then append word to a new text file.
    for check_word in words:
        if not check_word.lower() in stop:
            # Not found on stopword list, so append.
            appendFile = open(str(x)+'_bezs.txt', 'a', encoding='utf-8-sig')
            appendFile.write(" " +check_word)
            appendFile.close()
        else:
            # It's on the stopword list
            sw_found +=1
    return()

stopw('prva')
stopw('druga')
stopw('treca')
stopw('cetvrta')