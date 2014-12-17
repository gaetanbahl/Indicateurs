#!/usr/bin/python
# -*- coding:utf-8 -*-
import cgi, os
import cgitb; cgitb.enable()
import sqlite3
import time
from indicateurs import *
from datetime import date


def get_body ():
	form = cgi.FieldStorage(keep_blank_values    =    True)


	pole = form['pole'].value
	nomindic = form['nomindic'].value
	valeur_i = form['valeur_i'].value
	password =  form['password'].value

	d = date.fromtimestamp(time.time())
	fn = 'files/' + nomindic 
	fichier = open(fn, 'a+')
	fichier.write(valeur_i + " " + d.isoformat() + '\n')
	fichier.close()

	con = sqlite3.connect('bdd.db')
	cur = con.cursor()
	lignebdd =  'INSERT INTO INDICS VALUES ("{0}","{1}","{2}", "{3}");'.format(nomindic,pole,d.isoformat(),fn)

	cur.execute(lignebdd)    
	con.commit()

	return "L'indicateur {0} a été créé avec succès.".format(nomindic)

print    """\
Content-Type: text/html\n
<html><body>
<head>
        <meta charset="utf-8" />
</head>
<p>{0}</p>
</body></html>
""".format(get_body())
