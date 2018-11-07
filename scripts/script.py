import urllib
import re
import json
listOfDataToInsert=[]

def eliminate(link):
    f = urllib.urlopen(link)
    str = f.read()
    rez =  re.findall('404',str)
    if rez == []:
        return 1


def addDataInList(data):
    obj = {}
    list = data.split(",")

    for line in list:
        line =  line.split(":")
        if len(line) == 2:
            obj[line[0].replace("\n","").replace(" ","")] = line[1]

    print obj
    listOfDataToInsert.append(obj)


def extractData(link):
    link = link.replace("bibtex","bib2")
    f = urllib.urlopen(link)
    str = f.read()
    str = str[str.find(",") + 1:]
    data = str.replace("=",":").replace("}","").replace("{","")+","
    addDataInList(data)

def getLinkWithInfo(link):
    f = urllib.urlopen(link)
    str = f.read()

    #
    #   [^\s] mai putin
    #  ?/  se opreste de cel mai apropriat/
    #   () un group pe care il vreau sa il evidentiez (bibtex)
    #   r'' match-ul
    rez =  re.findall(r'href=\"https://[^\s]*?/bibtex/journals/[^\s]*?\"',str)

    for link in rez:
        link = link.replace("\"","").replace("href=","")
        extractData(link)

        break

small_letters = map(chr, range(ord('a'), ord('z')+1))

for letter in small_letters:
    link = "https://dblp.uni-trier.de/pers?prefix="+letter
    f = urllib.urlopen(link)
    str = f.read()
    rezVect =  re.findall(r'[a-zA-Z0-9]*, [a-zA-Z0-9]*',str)

    for name in rezVect:
        name = name.replace(", ", ":")
        link = 'https://dblp.uni-trier.de/pers/hd/' + letter + '/'  + name
        if eliminate(link):
            getLinkWithInfo(link)

    break



