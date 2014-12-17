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


	nomindic = form['indic'].value
	password =  form['password'].value

	os.system("rm files/{0}".format(nomindic))

	con = sqlite3.connect('bdd.db')
	cur = con.cursor()
	d = date.fromtimestamp(time.time())
	lignebdd =  'DELETE FROM INDICS WHERE indic="{0}";'.format(nomindic)

	cur.execute(lignebdd)    
	con.commit()

	return "L'indicateur {0} a été supprimé avec succès.".format(nomindic)

print    """\
Content-Type: text/html\n
<html><body>
<head>
        <meta charset="utf-8" />
</head>
<p>{0}</p>
</body></html>
""".format(get_body())
