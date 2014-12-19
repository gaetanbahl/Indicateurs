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
	form = cgi.FieldStorage(keep_blank_values = True)

	nomindic = form['indic'].value
	password =  form['password'].value

	if password != getpassword("qualite"):
		return "Mot de passe incorrect"

	con = sqlite3.connect('bdd.db')
	cur = con.cursor()
	d = date.fromtimestamp(time.time())
	lignebdd =  'DELETE FROM INDICS WHERE indic="{0}";'.format(nomindic)
	cur.execute(lignebdd)    
	con.commit()

	call(["rm","files/{0}".format(nomindic)])
	call(["rm","files/{0}.gnu".format(nomindic)])
	call(["rm","files/{0}.png".format(nomindic)])
	
	return "L'indicateur {0} a été supprimé avec succès.".format(nomindic)

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
