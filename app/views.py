# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import requests
import xmltodict
from bs4 import BeautifulSoup  as BS #analizar documentos html
from django.contrib.staticfiles import finders
from django.db.models import Q
import re
import time
import json
import os

#models
from app.models import *

# Create your views here.

domain = 'http://www.openculture.com/'

def scrapy_courses(request):
	url = domain + 'freeonlinecourses'
	web = requests.get(url)
	content = web.content
	
	'''
	para leer un archivo ubicado en la carpeta static

	urlFile = finders.find('1.txt')
	file = open(urlFile, "r")
	content = file.read()
	''' 

	soup = BS(content,'html.parser')


	courses = soup.find_all('div',{'class':'curatedcategory'})
	print len(courses), 'longitud'
	for dom in courses:
		try:
			h2 = dom.find('h2')

			a = h2.find('a')

			#saving Categoria
			categoryname = h2.get_text()
			newCat = Categories(name = categoryname)

			#Comprobando nuevas categorias
			categoryDB = Categories.objects.filter(name=categoryname)
			

			if categoryDB == None:
				print 'Nueva Categoria encontrada'
				newCat.save()

			else:
				newCat = categoryDB[0]

			#print newCat.name

			uls = dom.find_all('ul')
			#recorriendo los ULs
			for x in uls:
				#recorriendo los LIs
				for li in x.find_all('li'):
					try:
						#Comprobando si dentro de un li hay un ul
						ulonli = li.find('ul')
						for j in ulonli.find_all('li'):
							findCourses(j, newCat)
					except Exception as e:
						#sigue su trancurso normal
						findCourses(li, newCat)
			
			print '\n'

		except Exception as e:
			print '\n'
			#print dom
			print 'ERROR --------->', e
	
			


		

	return HttpResponse('Ends')

def findCourses(LI, category):
	#titulo de curso
	title_course = LI.find('strong').get_text()

	#encontrando autores
	listLI = LI.get_text().split('-')
	idx = len(listLI) - 1
	author=  listLI[idx]

	courseDB = Courses.objects.filter(name=title_course, authors=author)
	if courseDB == None:
		print 'Nuevo curso detectado'
		newCourse = Courses()
		newCourse.name = title_course
		newCourse.authors = author
		newCourse.category = category
		newCourse.save()

		print newCourse.name + ' a-> ' + author

		#encontrando los links
		tagAlist = LI.find_all('a')
		for a in tagAlist:
			nameLink = a.get_text()
			url = a.get('href')

			newLink = Linkcourses()
			newLink.namelink = nameLink
			newLink.url = url
			newLink.course = newCourse
			newLink.save()
			print '\t' + newLink.namelink

		
		print 'Saved Course' + title_course
		print '\n'



def scrapy_audio_books(request):
	url = domain + 'freeaudiobooks'
	web = requests.get(url)
	content = web.content

	soup = BS(content,'html.parser')

	div_main = soup.find('div',{'class':'entry'})

	dom_ULs = div_main.find_all('ul')

	for ul in dom_ULs:
		dom_LIs = ul.find_all('li')
		for li in dom_LIs:
			textLI = li.get_text()
				
			titleAudio = ''
			rowLI = textLI.split(' - ')
			if len(rowLI) > 1:
				authorAudio = rowLI[0]
				titleAudio = rowLI[1]


				newAudioBook = Audiobooks()
				newAudioBook.title = titleAudio
				newAudioBook.authors = authorAudio
				newAudioBook.save()

				#Encontrando los enlaces del recurso
				for a in li.find_all('a'):
					nameLink = a.get_text()
					url = a.get('href')

					newLinkAudio = Linkaudios()
					newLinkAudio.namelink = nameLink
					newLinkAudio.url = url
					newLinkAudio.audiobook = newAudioBook
					newLinkAudio.save()

				print '\nAudio Obj Saved:\n' , newAudioBook
				

				#el html no tiene un formato adecuado, para la cual se decidio 
				#encontrar al utlmimo audiobook, para finalizar el proceso
				if authorAudio == 'Wittgenstein, Ludwig':
					return HttpResponse('LLegando Al ultimo ID')


	return HttpResponse('Ok End')

def findTipoCredencial(lstCredentials, valor):
	for c in lstCredentials:
		if c.acronym == valor:
			return c
	return None


def scrapy_moocs(request):
	jsonFile = [{
			"id" : 1,
			"name" : "Certificate of Completion",
			"acronym" : "CC"
		},
		{
			"id" : 2,
			"name" : "Certificate of Accomplishment",
			"acronym" : "CA"
		},
		{
			"id" : 3,
			"name" : "Honor Code Certificate",
			"acronym" : "HCC"
		},
		{
			"id" : 4,
			"name" : "Verified Certificate",
			"acronym" : "VC$"
		},
		{
			"id" : 5,
			"name" : "Verified Certificate of Accomplishment",
			"acronym" : "VCA$"
		},
		{
			"id" : 6,
			"name" : "Statement of Accomplishment",
			"acronym" : "SA"
		},
		{
			"id" : 7,
			"name" : "Statement of Participation",
			"acronym" : "SP$"
		},
		{
			"id" : 8,
			"name" : "Certificate of Mastery",
			"acronym" : "CM"
		},
		{
			"id" : 9,
			"name" : "No Information About Certificate Available",
			"acronym" : "NI"
		},
		{
			"id" : 10,
			"name" : "No Certificate",
			"acronym" : "NC"
		},
		{
			"id" : 11,
			"name" : "No Definido",
			"acronym" : ""
		},
		{
			"id" : 12,
			"name" : "Statement of Accomplishment /  Verified Certificate",
			"acronym" : "SA/VC$"
		},
		{
			"id" : 13,
			"name" : "Honor Code Certificate / Verified Certificate",
			"acronym" : "HCC/VC$"
		}
	]

	listCredentials = []

	for x in jsonFile:
		credentialOBJ = Credentialskey()
		credentialOBJ.id = x['id']
		credentialOBJ.name = x['name']
		credentialOBJ.acronym = x['acronym']
		listCredentials.append(credentialOBJ)
	
	urlWeb = domain + 'free_certificate_courses'
	web = requests.get(urlWeb)
	content = web.content

	soup = BS(content,'html.parser')

	div_main = soup.find('div',{'class':'entry'})

	dom_ULs = div_main.find_all('ul')

	for ul in dom_ULs:
		dom_LIs = ul.find_all('li')
		for li in dom_LIs:

			credentialTxt = ''
			offer = ''
			date = ''

			dom_Span = li.find_all('span')
			if len(dom_Span) > 1:
				titleMooc = dom_Span[0].find('a').get_text()
				linkMooc = dom_Span[0].find('a').get('href')

				try:
					lastSpanIdx = len(dom_Span) - 1
					lstSplit = dom_Span[lastSpanIdx].get_text().split(' - ')
					credentialTxt = lstSplit[0]
					offer = lstSplit[1]
					date = lstSplit[2]

					#obteniedo el tipo de certificado
					lastCharacter = len(credentialTxt)
					credential = credentialTxt[2:lastCharacter- 1]
					
					tipoCredentialOBJ = findTipoCredencial(listCredentials, credential)
					if tipoCredentialOBJ == None:
						#asignando objeto no Definido
						tipoCredentialOBJ = findTipoCredencial(listCredentials, 'No Definido')

					newMooc = Moocs()
					newMooc.title = titleMooc
					newMooc.offer = offer
					newMooc.date = date
					newMooc.link = linkMooc
					newMooc.credentialskey = tipoCredentialOBJ
					newMooc.save()

					print titleMooc, ' - ', credentialTxt, ' - ', offer,' - ', date, ' - ', tipoCredentialOBJ.name
					print 'Saved\n'

				except Exception as e:
					print e
					print 'Algo esta mal ERROR :('


	return HttpResponse('End Search ...')


def scrapy_movies(request):
	url = domain + 'freemoviesonline'
	web = requests.get(url)
	content = web.content

	soup = BS(content,'html.parser')

	domCategories = soup.find_all('div',{'class':'curatedcategory'})

	print len(domCategories)

	for cat in domCategories:
		try:
			h2 = cat.find('h2')
			a = h2.find('a')
			#saving Categoria
			categoryname = a.get_text()
			newCategoryObj = Categories()
			newCategoryObj.name = categoryname
			newCategoryObj.save()
			print 'Saved Category', categoryname

			dom_ULs = cat.find_all('ul')
			for ul in dom_ULs:
				dom_LIs = ul.find_all('li')
				for li in dom_LIs:
					titleMovie = li.find('strong').get_text()
					linkMovie = li.find('a').get('href')
					
					liText = li.get_text()

					start = liText.find('Free') + 7
					descriptionMovie = liText[start:]

					newMovieObj = Movies()
					newMovieObj.title = titleMovie
					newMovieObj.url = linkMovie
					newMovieObj.description = descriptionMovie
					newMovieObj.category = newCategoryObj
					newMovieObj.save()

					print titleMovie
					print linkMovie
					print descriptionMovie
					print 'Movie saved!!'
		except Exception as e:
			print e
	
	return HttpResponse('Listo! ')


def scrapy_languajes(request):
	urlWeb = domain + 'freelanguagelessons'
	web = requests.get(urlWeb)
	content = web.content

	soup = BS(content,'html.parser')

	div_main = soup.find('div',{'class':'entry'})

	dom_Ps = div_main.find_all('p')
	#encontrando categorias
	lstCategoriesLanguajes = []
	for p in dom_Ps:
		try:
			cat = p.find('span').find('strong').get_text()
			lstCategoriesLanguajes.append(cat)
		except Exception as e:
			print e

	#encontrando los listados de los cursos
	dom_ULs = div_main.find_all('ul')
	cont = 1
	for ul in dom_ULs:
		dom_LIs = ul.find_all('li')
		for li in dom_LIs:
			try:
				dom_UL_on_LI = li.find_all('ul')
				if len(dom_UL_on_LI) >= 1:
					print cont
					cont = cont + 1
					#Entonces vamos a trabajar con este LI
					titleCourseLan = li.find('strong').get_text()
					print '\t', titleCourseLan 
					dom_A = li.find_all('a')
					for a in dom_A:
						nammUrlLa =a.get_text()
						print '\t\t',nammUrlLa
						

			except Exception as e:
				#No es el primer UL, no nos sirve esta repitiendo el contenido
				print ''

	print 'len lstCategorias: ', len(lstCategoriesLanguajes)
	print 'len Uls: ', len(dom_ULs)
	

	return HttpResponse('END .. ')
