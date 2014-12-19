#!/usr/bin/python2
# -*- coding: utf8 -*- 
import sqlite3,cgitb
cgitb.enable()
from indicateurs import *
con = sqlite3.connect("/var/www/html/Indicateurs/bdd.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("SELECT * FROM INDICS;")

rows = cur.fetchall()

								
print """\
Content-Type: text/html\n
<html>
<head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
</head>


<body>
	<header>
		<a href='index.html'><img src="indicateurs.png"/></a>
	</header>

	<nav>
		<div class='menu'><a href='index.html'>Accueil</a><br/></div>
		<div class='menu'><a href='look.cgi'>Consulter</a><br/></div>
		<div class='menu'><a href='upload.py'>Relever</a><br/></div>
	</nav>
	
	<section>
		
		
		<article class="poil">
			<h1>Consulter les indicateurs relevés</h1>
			<table>
				   <tr>
					   <td><b>Indicateur</b></td>
					   <td><b>Pôle</b></td>
					   <td><b>Dernière update</b></td>
					   <td><b>Graphe</b></td>
				   </tr>"""
				   
				   
for row in rows:
        print u'<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>'.format(row["indic"], unicode(short_to_pole(row["pole"]),'utf-8'), row["date"], "<a href=\""+row["file"]+'.png">PNG</a>').encode('utf-8')
				   
				   
				   
				   
				   
print """				   
				</table>
							
		</article>
	</section>
<footer>
Par Gaétan, directeur du Pôle Qualité.
</footer>

</body>

</html>

""" 
