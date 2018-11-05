import urllib
import json
import pprint
import mysql.connector

#
#create table information ( id int, score int, author  varchar(500), title   varchar(500), venue   varchar(500), volume  varchar(500), pages   int, year    int, type varchar(255), site varchar(255))

link = "http://dblp.org/search/publ/api?q=a&c=100000&format=json"
f = urllib.urlopen(link)
str = f.read()
obj = json.loads(str)


id      =  obj['result']['hits']['hit'][0]['@id']
score   =  obj['result']['hits']['hit'][0]['@score']
author  =  obj['result']['hits']['hit'][0]['info']['authors']['author'][0]
title   =  obj['result']['hits']['hit'][0]['info']['title']
venue   =  obj['result']['hits']['hit'][0]['info']['venue']
volume  =  obj['result']['hits']['hit'][0]['info']['volume']
pages   =  obj['result']['hits']['hit'][0]['info']['pages']
year    =  obj['result']['hits']['hit'][0]['info']['year']
type    =  obj['result']['hits']['hit'][0]['info']['type']
site    =  obj['result']['hits']['hit'][0]['info']['ee']


cnx = mysql.connector.connect(user='root', host='127.0.0.1', database='bigdata')

mycursor = cnx.cursor()



mycursor.execute("SELECT * FROM information where id = '%s'",(id))
myresult = mycursor.fetchall()
pprint.pprint(myresult)

if myresult == []:
    sql = "INSERT INTO information (id, score, author, title, venue, volume, pages, year, type, site) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (id, score, author, title, venue, volume, 10, year, type, site)
    mycursor.execute(sql, val)

cnx.commit()
