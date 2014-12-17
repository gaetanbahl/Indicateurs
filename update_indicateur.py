#!/usr/bin/python
# -*-encoding:utf-8 -*-
import cgi, os
import cgitb; cgitb.enable()
import sqlite3
import time
from datetime import date


def get_body ():
	form = cgi.FieldStorage(keep_blank_values    =    True)


	pole = form['pole'].value
	indic = form['indic'].value
	valeur = form['valeur'].value
	password =  form['password'].value
	d = date.fromtimestamp(time.time())

	fn = 'files/' + indic 
	fichier = open(fn, 'a+')
	fichier.write(valeur + " " +  d.isoformat() + "\n")
	fichier.close()

	con = sqlite3.connect('bdd.db')
	cur = con.cursor()
	lignebdd =  'UPDATE INDICS SET  date="{0}" WHERE indic="{1}";'.format( d.isoformat(), indic)

	cur.execute(lignebdd)    
	con.commit()

	return "L'indicateur {0} a été mis à jour avec succès.".format(indic)

print    """\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8" />
</head>
<body><p>{0}</p>
</body></html>
""".format(get_body())
