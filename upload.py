#!/usr/bin/python
# -*- coding:utf8 -*-
								
import sqlite3
from datetime import date
from indicateurs import *
con = sqlite3.connect("bdd.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("SELECT * FROM INDICS;")

rows = cur.fetchall()

d = date.today()

liste_indics=""

for row in rows:
	liste_indics += u'<option value="{0}">{0}</option> \n'.format(row["indic"]).encode('utf-8')

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
		
		
		<article>
			<h1> Relever un indicateur </h1>
			<form enctype="multipart/form-data" action="update_indicateur.py" method="post">
				<p>Pôle : <select name="pole" id="pole"> 
						<option value="president">Président</option>
						<option value="commercial">Commercial</option>
						<option value="qualite">Qualité</option>
						<option value="secretariat">Secrétariat</option>
						<option value="treso">Trésorerie</option>
						<option value="com">Communication</option>
						<option value="prosp">Prospection</option>
						<option value="dsi">DSI</option>
						<option value="rh">Ressources Humaines</option>
				</select>
				<p>Date (jour, mois, année): <input name="jour" size="2" value="{1}"/><input name="mois" size="2" value="{2}"/><input name="annee" size="4" value="{3}"/>


</p 
				<p> Indicateur : <select id="indic" name="indic">
					{0}
				</select>
				
<p>Nouvelle valeur : <input type="text" name="valeur" size="4"></p>
				<p>Mot de passe : <input name="password" size="4" /> </p>
				
				<p><input type="submit" value="Relever"></p>
			</form>
			
		</article>
	</section>
<footer>
Par Gaétan, directeur du Pôle Qualité.
</footer>

</body>

</html>

""".format(liste_indics,d.day,d.month,d.year ) 
