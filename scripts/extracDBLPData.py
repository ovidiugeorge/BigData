import urllib
import json
import pprint
import mysql.connector

#
#create table information ( id int, score int, author  varchar(500), title   varchar(500), venue   varchar(500), volume  varchar(500), pages   int, year    int, type varchar(255), site varchar(255))
cnx = mysql.connector.connect(user='root', host='127.0.0.1', database='bigdata')
mycursor = cnx.cursor()
small_letters = map(chr, range(ord('a'), ord('z')+1))
for c in small_letters:
    link = "http://dblp.org/search/publ/api?q="+c+"&c=100000&format=json"
    f = urllib.urlopen(link)
    str = f.read()
    obj = json.loads(str)



    for i in range(0,len(obj['result']['hits']['hit'])):
        keys = (obj['result']['hits']['hit'])[i].keys()

        if '@id' in keys:
            id  =  obj['result']['hits']['hit'][i]['@id']
        else :
            continue

        if '@score' in keys:
            score   =  obj['result']['hits']['hit'][i]['@score']
        else :
            continue

        if 'author' in (obj['result']['hits']['hit'][i]['info']['authors']).keys():
            author  =  obj['result']['hits']['hit'][i]['info']['authors']['author'][0]
        else :
            continue

        keys = (obj['result']['hits']['hit'][i]['info']).keys()
        if 'title' in keys:

            if (obj['result']['hits']['hit'][i]['info']['title']).isnumeric():
                continue
            else:
                title = obj['result']['hits']['hit'][i]['info']['title']
        else:
            continue

        if 'venue' in keys:
            venue   =  obj['result']['hits']['hit'][i]['info']['venue']
        else :
            continue

        if 'volume' in keys:
            volume  =  obj['result']['hits']['hit'][i]['info']['volume']
        else :
            continue

        if 'pages' in keys:
            pages   =  2#obj['result']['hits']['hit'][i]['info']['pages']
        else :
            continue

        if 'year' in keys:
            year    =  obj['result']['hits']['hit'][i]['info']['year']
        else :
            continue

        if 'type' in keys:
            type    =  obj['result']['hits']['hit'][i]['info']['type']
        else :
            continue

        if 'ee' in keys:

            site    =  obj['result']['hits']['hit'][i]['info']['ee']
        else :
            continue

        print i

        sql = "SELECT * FROM information where id = "+id;
        mycursor.execute(sql)
        myresult = mycursor.fetchall()


        if myresult == []:
            sql = "INSERT INTO information (id, score, author, title, venue, volume, pages, year, type, site) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (id, score, author, title, venue, volume, 10, year, type, site)
            try:
                mycursor.execute(sql, val)
                print 'add'
            except:
                continue
        else :
            print 'added'

        print "\n"




cnx.commit()
