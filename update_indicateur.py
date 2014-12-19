#!/usr/bin/python
# -*-encoding:utf-8 -*-
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
	indic = form['indic'].value
	valeur = form['valeur'].value
	password =  form['password'].value
	annee = form['annee'].value
	mois = form['mois'].value
	jour = form['jour'].value
	
	d = date.fromtimestamp(time.time())

	fn = 'files/' + indic 

	con = sqlite3.connect('bdd.db')
	con.row_factory = sqlite3.Row
	cur = con.cursor()

	lignebddverify = 'SELECT * FROM INDICS WHERE indic="{0}"'.format(indic)
	cur.execute(lignebddverify)    
	rows = cur.fetchall()
	for i in rows:
		if i["pole"] != pole:
			return "Votre pole n'a pas le droit de modifier cet indicateur !"
	
	if password != getpassword(pole): 
		return "Mot de passe incorrect"


	lignebdd =  'UPDATE INDICS SET  date="{0}" WHERE indic="{1}";'.format( d.isoformat(), indic)

	cur.execute(lignebdd)    
	con.commit()
	
	fichier = open(fn, 'a+')
	if jour < 10:
		fichier.write(valeur + " " + str(annee) + str(mois) + "0" + str(jour) + "\n")
	else:
		fichier.write(valeur + " " + str(annee) + str(mois) + str(jour) + "\n")
	fichier.close()

	sortindicfile(fn)
	
	call(['gnuplot',fn + '.gnu'])
	
	#call(['convmv', '-t' ,'UTF-8', '-f', 'ISO-8859-1' ,fn + '.png'])

	return "L'indicateur {0} a été mis à jour avec succès.".format(indic)

print    """\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8" />
<meta http-equiv="refresh" content="3; URL=look.cgi">
</head>
<body><p>{0}</p>
Redirection dans 3 secondes.
</body></html>
""".format(get_body())
