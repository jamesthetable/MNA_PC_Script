#!/user/bin/python 
# coding: utf-8

import csv
import requests
import os
from bs4 import BeautifulSoup

n = 0

entetes = {
	"User-Agent":"Dominique Degré - journaliste à La Presse Canadienne",
	"From":"d.degre95@gmail.com"
}

for i in range(1,4):
	fich = "assnat{}.html".format(i)
	# print(fich)
	page = BeautifulSoup(open(fich),"html.parser")
	for ligne in page.find_all("tr"):
		url = ligne.a["href"]
		if url.startswith("http://www.assnat.qc.ca/fr/travaux-parlementaires/assemblee-nationale/41-1/journal-debats/201"):
			n += 1
			print(n,url)
			"http://www.assnat.qc.ca/fr/travaux-parlementaires/assemblee-nationale/41-1/journal-debats/20170426/196023.html"
			date = url[-20:-12]
			print(date)

			c = requests.get(url,entetes)
			page2 = BeautifulSoup(c.text,"html.parser")
			
			os.remove("deputes-liste.csv")
			os.rename("deputes-liste-final.csv","deputes-liste.csv")

			fichier1 = "deputes-liste.csv"
			f1 = open(fichier1)
			fichier2 = "deputes-liste-final.csv"
			deputes = csv.reader(f1)
			x = 0
			for depute in deputes:

				x += 1
				if x == 1:
					ligne = depute
					ligne.append(date)
					gaston = open(fichier2,"a")
					lagaffe = csv.writer(gaston)
					lagaffe.writerow(ligne)
					print(ligne)
				else:
					presences = 0
					# print(depute[0])
					elu = "{} ({})".format(depute[0],depute[2].replace(" ", u"\xa0"))
					elu2 = "{} \n({})".format(depute[0],depute[2].replace(" ", u"\xa0"))
					elu3 = "{}\n ({})".format(depute[0],depute[2].replace(" ", u"\xa0"))
					elu4= "{} ({})".format(depute[0],depute[2].replace(u"\xa0"," "))
					elu5= "{} ({})".format(depute[0].replace(" ",u"\xa0"),depute[2])
					elu6= "{} ({})".format(depute[0],depute[2].replace("\n"," "))
					# print(elu)

					for p in page2.find_all("p"):

						if elu in p.text:
							presences += 1
						elif elu2 in p.text:
							presences += 1
						elif elu3 in p.text:
							presences += 1
						elif elu4 in p.text:
							presences+=1
						elif elu5 in p.text:
							presences+=1
						elif elu6 in p.text:
							presences+=1
							
					for p in page2.find_all("b"):

						if elu in p.text:
							presences -= 1
						elif elu2 in p.text:
							presences -= 1
						elif elu3 in p.text:
							presences -= 1
						elif elu4 in p.text:
							presences-=1
						elif elu5 in p.text:
							presences-=1
						elif elu6 in p.text:
							presences-=1
							# print(p.text.strip())

					ligne = depute
					ligne.append(presences)
					gaston = open(fichier2,"a")
					lagaffe = csv.writer(gaston)
					lagaffe.writerow(ligne)
					print(ligne)