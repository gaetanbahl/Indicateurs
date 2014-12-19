#!/usr/bin/python
# -*- coding:utf-8 -*-
import cgi, os
import cgitb; cgitb.enable()
import sqlite3
import time
from indicateurs import *
from datetime import date
from subprocess import call

def get_body ():
	form = cgi.FieldStorage(keep_blank_values    =    True)


	pole = form['pole'].value
	nomindic = form['nomindic'].value
	valeur_i = form['valeur_i'].value
	password =  form['password'].value

	d = date.fromtimestamp(time.time())
	fn = 'files/' + nomindic 

	if password != getpassword("qualite"):
		return "Mot de passe incorrect"

	con = sqlite3.connect('bdd.db')
	cur = con.cursor()
	lignebdd =  'INSERT INTO INDICS VALUES ("{0}","{1}","{2}", "{3}");'.format(nomindic,pole,d.isoformat(),fn)

	cur.execute(lignebdd)    
	con.commit()

	fichier = open(fn, 'a+')
	if d.day < 10:
		fichier.write(valeur_i + " " + str(d.year) + str(d.month) + "0" + str(d.day) + '\n')
	else:
		fichier.write(valeur_i + " " + str(d.year) + str(d.month) + str(d.day) + '\n')
	fichier.close()
	
	call(['files/plottage.sh',fn])
	call(['gnuplot',fn+'.gnu'])

	return "L'indicateur {0} a été créé avec succès.".format(nomindic)

print    """\
Content-Type: text/html\n
<html><body>
<head>
        <meta charset="utf-8" />
<meta http-equiv="refresh" content="3; URL=admin.py">
</head>
<p>{0}</p>
Redirection dans 3 secondes.
</body></html>
""".format(get_body())
