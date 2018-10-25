import urllib
import re

def eliminate(link):
    f = urllib.urlopen(link)
    str = f.read()
    rez =  re.findall('404',str)
    if rez == []:
        return 1

def getLinkWithInfo(link):
    f = urllib.urlopen(link)
    str = f.read()

    #
    #   [^\s] mai putin
    #  ?/  se opreste de cel mai apropriat/
    #   () un group pe care il vreau sa il evidentiez (bibtex)
    #   r'' match-ul

    rez =  re.findall(r'href=\"https://[^\s]*?/xml/journals/[^\s]*?\"',str)
    for name in rez:
        print name,"\n\n\n"



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



