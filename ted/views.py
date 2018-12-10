# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup  as BS
from django.utils import timezone
from ted.models import *

import requests
import xmltodict
import json
import urllib2



domain = 'https://www.ted.com/'
#Recuperando las listas de comprobación
lstRatings = list(Ratings.objects.all())
lstTags = list(Tags.objects.all())
lstLanguages = list(TalkLanguages.objects.all())
lstSpeakers = list(Speakers.objects.all())

# Create your views here.

def checkExistRating(lista, nombre):
	for x in lista:
		if x.name == nombre:
			return x
	rtObj = Ratings()
	rtObj.name = nombre
	rtObj.save()
	lstRatings.append(rtObj)
	return rtObj

def checkExistTag(lista, nombre):
	for x in lista:
		if x.name == nombre:
			return x
	tagObj = Tags()
	tagObj.name = nombre
	tagObj.save()
	lstTags.append(tagObj)
	return tagObj

def checkExistSpeaker(lista, exponenteObj):
	for x in lista:
		id_1 = x.speaker_id
		id_2 = int(exponenteObj.speaker_id)
		if id_1 == id_2:
			return x
	exponenteObj.save()
	lstSpeakers.append(exponenteObj)
	return exponenteObj

def checkExistLanguaje(lista, nombre,endonimo,codigo,ianacodigo):
	for x in lista:
		if x.languagename == nombre and x.endonym == endonimo and x.languagecode == codigo and x.ianacode == ianacodigo:
			return x
	tLObj = TalkLanguages()
	tLObj.languagename = nombre
	tLObj.endonym = endonimo
	tLObj.languagecode = codigo
	tLObj.ianacode = ianacodigo
	tLObj.save()
	lstLanguages.append(tLObj)
	return tLObj


def scrapy_ted_detail(enlaceTed):

	#url = 'https://www.ted.com/talks/bill_gates_unplugged'
	web = requests.get(enlaceTed)
	content = web.content

	soup = BS(content,'html.parser')

	scripts = soup.find_all('script')

	data = {}

	for sc in scripts:
		txtScript = sc.get_text()
		if txtScript[:19] == 'q("talkPage.init", ':
			limit = len(txtScript) - 1
			txtJson = txtScript[19:limit]
			data = json.loads(txtJson)
			#print txtJson
	print 'Data Ready! ', len(data)
	
	while len(data) == 0:
		print 'De NUEVO'
		web = requests.get(enlaceTed)
		content = web.content

		soup = BS(content,'html.parser')

		scripts = soup.find_all('script')

		data = {}

		for sc in scripts:
			txtScript = sc.get_text()
			if txtScript[:19] == 'q("talkPage.init", ':
				limit = len(txtScript) - 1
				txtJson = txtScript[19:limit]
				data = json.loads(txtJson)
	#print data
	try:
		#get data of Talk
		talkJson = data['__INITIAL_DATA__']
		talkData = data['__INITIAL_DATA__']['talks'][0]
		
		idCharla = talkJson['current_talk']
		idHilo = talkJson['threadId']
		if talkJson['comments'] == None:
			numComentarios = 0
		else:
			numComentarios = talkJson['comments']['count']
		tituloCharla = talkData['title']
		descripcionCharla = talkJson['description']
		evento = talkJson['event']
		lenguaje = talkJson['language']
		postaCharla = talkJson['slug']
		curadorAprobado = talkData['curator_approved']
		nombreSocioInstituto = talkData['institute_partner_name']
		duracion = talkData['duration']
		nombreSalonInstituto = talkData['salon_partner_name']
		insigniaEvento = talkData['event_badge']
		seOfrece = talkData['is_featured']
		nombreCharla = talkJson['name']
		protagonistaFoto = talkData['hero']
		protagonistaFotoCargando = talkData['hero_load']
		gurdadoEn = talkData['recorded_at']
		tipoVideo = talkData['video_type']['name']
		urlCharla = talkJson['url']
		contadorVisitas = talkJson['viewed_count']


		#build the object Talk
		talkObj = Talks()
		talkObj.talk_id = idCharla
		talkObj.threadid = idHilo
		talkObj.num_comments = numComentarios
		talkObj.title = tituloCharla
		talkObj.description = descripcionCharla
		talkObj.event = evento
		talkObj.language = lenguaje
		talkObj.slug = postaCharla
		talkObj.institute_partner_name = nombreSocioInstituto
		talkObj.duration = duracion
		talkObj.salon_partner_name = nombreSalonInstituto
		talkObj.event_badge = insigniaEvento
		talkObj.is_featured = seOfrece
		talkObj.name = nombreCharla
		talkObj.hero = protagonistaFoto
		talkObj.hero_load = protagonistaFotoCargando
		talkObj.recorded_at = gurdadoEn
		talkObj.video_type = tipoVideo
		talkObj.viewed_count = contadorVisitas
		talkObj.curator_approved = curadorAprobado
		talkObj.url_talk = urlCharla
		talkObj.row_inserted = timezone.now()
		talkObj.save()
		'''
		print idCharla, '\n->' , idHilo, '\n->' ,numComentarios, '\n->' ,tituloCharla
		print '->',descripcionCharla, '\n->' , evento, '\n->' , lenguaje, '\n->' , postaCharla
		print '-> Curator: ',curadorAprobado, '\n->SociIns' , nombreSocioInstituto, '\n->' , duracion, '\n->Salon' , nombreSalonInstituto
		print '->Insignia',insigniaEvento, '\n->' , seOfrece, '\n->' , nombreCharla
		print '->',protagonistaFoto, '\n->' , protagonistaFotoCargando
		print '->',gurdadoEn, '\n->' , tipoVideo, '\n->' , urlCharla, '\n->' , contadorVisitas
		'''
		#get data of Speaker
		speakerJson = data['__INITIAL_DATA__']['speakers']
		for s in speakerJson:
			idExpositor = s['id']
			posta = s['slug']
			publicado = s['is_published']
			nombre = s['firstname']
			apellido = s['lastname']
			inicialMedio = s['middleinitial']
			titulo = s['title']
			descripcion = s['description']
			urlFoto = s['photo_url']
			loQueDigas = s['whatotherssay']
			quienEs = s['whotheyare']
			porqueEscuchar = BS(s['whylisten'],'html.parser').get_text()

			#build the object Speaker
			speakerObj = Speakers()
			speakerObj.speaker_id = idExpositor
			speakerObj.slug = posta
			speakerObj.is_published = publicado
			speakerObj.firstname = nombre
			speakerObj.lastname = apellido
			speakerObj.middleinitial = inicialMedio
			speakerObj.title = titulo
			speakerObj.description = descripcion
			speakerObj.photo_url = urlFoto
			speakerObj.whatotherssay = loQueDigas
			speakerObj.whotheyare = quienEs
			speakerObj.whylisten = porqueEscuchar
			speakerObj = checkExistSpeaker(lstSpeakers, speakerObj)

			thsObj = TalksHasSpeakers()
			thsObj.talks = talkObj
			thsObj.speakers = speakerObj
			thsObj.save()



		#print idExpositor, '\n->' ,posta, '\n->' ,publicado, '\n->' ,nombre, '\n->' ,apellido, '\n->' ,inicialMedio, '\n->' ,titulo, '\n->' ,descripcion, '\n->' ,urlFoto, '\n->' ,loQueDigas, '\n->' ,quienEs, '\n->' ,porqueEscuchar

		#get related talks
		relatedTalksJson = talkData['related_talks']
		for rt in relatedTalksJson:
			relatedTalksObj = RelatedTalks()
			relatedTalksObj.talk_id = rt['id']
			relatedTalksObj.title = rt['title']
			relatedTalksObj.speaker = rt['speaker']
			relatedTalksObj.duration = rt['duration']
			relatedTalksObj.slug = rt['slug']
			relatedTalksObj.talks = talkObj
			relatedTalksObj.save()

			'''print idRTalk
			print tituloRTalk
			print exponenteRTalk
			print duracionRTalk
			print postaRTalk,'\n' '''

		#get Ratings
		ratingsJson = talkData['ratings']
		for r in ratingsJson:
			thrObj = TalksHasRatings()
			thrObj.talks = talkObj
			thrObj.ratings = checkExistRating(lstRatings,r['name'])
			thrObj.count = r['count']
			thrObj.save()
			#print nombreClasificacion, ' - ', contadorClasificacion

		#get Tags
		tagsJson = talkData['tags']
		for t in tagsJson:
			thtObj = TalksHasTags()
			thtObj.talks = talkObj
			thtObj.tags = checkExistTag(lstTags,t)
			thtObj.save()

		dataDownloads = talkData['downloads']

		#get Languages
		languagesJson = dataDownloads['languages']
		for l in languagesJson:
			nombreIdioma = l['languageName']
			endonimoIdioma = l['endonym']
			codigoIdioma = l['languageCode']
			ianaCodigo = l['ianaCode']

			thlaObj = TalksHasLanguages()
			thlaObj.talks = talkObj
			thlaObj.languages = checkExistLanguaje(lstLanguages,nombreIdioma,endonimoIdioma,codigoIdioma,ianaCodigo)
			thlaObj.isrtl = l['isRtl']
			thlaObj.save()
			#print nombreIdioma, ' - ', endonimoIdioma, ' - ', codigoIdioma, ' - ', ianaCodigo

		#get Downloads Subtitles
		if dataDownloads['subtitledDownloads'] != None:
			subtitledDownloads = dataDownloads['subtitledDownloads']
			for sd in subtitledDownloads:
				try:
					dtSubD = subtitledDownloads[sd]
					nombreSub = dtSubD['name']
					calidadBaja = dtSubD['low']
					calidadAlta = dtSubD['high']
					subDObj = SubtitledDownloads()
					subDObj.name = nombreSub
					subDObj.low = calidadBaja
					subDObj.high = calidadAlta
					subDObj.talks = talkObj
					subDObj.save()
				except Exception as e:
					print e
				#print nombreSub ,' - ' , calidadBaja, ' - ', calidadAlta

		#get Native Downloads
		if dataDownloads['nativeDownloads'] != None:
			nativeDownloads = dataDownloads['nativeDownloads']
			nativoDBajo = nativeDownloads['low']
			nativoDMedio = nativeDownloads['medium']
			nativoDAlto = nativeDownloads['high']
			audioDescarga = dataDownloads['audioDownload']

			natDObj = NativeDowloads()
			natDObj.low = nativoDBajo
			natDObj.medium = nativoDMedio
			natDObj.high = nativoDAlto
			natDObj.audiodownload = audioDescarga
			natDObj.talks = talkObj
			natDObj.save()

		print 'Guardado',talkObj.title
		
	except Exception as e:
		raise e
	#print nativoDBajo,'\n',nativoDMedio,'\n',nativoDAlto,'\n',audioDescarga
	

def scrapy_ted_taks(request):
	for x in xrange(90,96):
		url = 'https://www.ted.com/talks?page='+str(x)
		web = requests.get(url)
		content = web.content

		soup = BS(content,'html.parser')

		talks = soup.find_all('div',{'class':'talk-link'})
		#for t in talks[33:]:
		for t in talks:
			url_talk = 'https://www.ted.com'+t.find('a').get('href')
			print talks.index(t), ' - ', x
			print'-> Descargando: |', url_talk
			scrapy_ted_detail(url_talk)

	return HttpResponse('Listo')