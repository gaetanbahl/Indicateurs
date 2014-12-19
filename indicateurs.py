#!/usr/bin/python
# -*-coding:utf-8-*-

def short_to_pole(s):
	if s == "president":
		return "Président"
	elif s == "qualite":
		return "Qualité"
	elif s == "treso":
		return "Trésorerie"
	elif s == "com":
		return "Communication"
	elif s == "secretariat":
		return "Secrétariat"
	elif s == "prosp":
		return "Prospection"
	elif s == "dsi":
		return "Direction des Systèmes d'Information"
	elif s == "rh":
		return "Ressources Humaines"
	elif s == "commercial":
		return "Commercial"

def getpassword(s):

	fichier = open('../passwords','r')
	
	for line in fichier:
		l = line.split(' ')
		if l[0] == s:
			return l[1][:-1]

	fichier.close()

def sortindicfile(indic):
	f = open(indic,'r')
	lignes = []
	for ligne in f:
		lignes.append(ligne)

	splittage = []
	for i in lignes:
		i2 = i.split(' ')
		splittage.append((i2[0],i2[1][:-1]))

	splittage.sort(key=lambda tup: tup[1])

	f.close()
	f = open(indic, 'w')
	for i in splittage:
		f.write(i[0] + " " + i[1] + "\n")

	f.close()
