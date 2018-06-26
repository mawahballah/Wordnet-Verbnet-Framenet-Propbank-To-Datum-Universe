import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union
doneantonyms={}
def Getexactkatum(synset):
	name=synset.name()
	word=name.split('.')[0]
	wordkatum=wordroot.find(word)
	if(wordkatum!=None):
		synsetdefinition=synset.definition()
		for instance in wordkatum.I:
			instancedefinition=definition.of(instance)
			if(instancedefinition!=None and instancedefinition.O==synsetdefinition):
				return instance				
	return None

def addhyponyms(synset):	
	exacthypernymkatum=Getexactkatum(synset)
	if(exacthypernymkatum!=None):
		for hyponym in synset.hyponyms():
			exacthyponymkatum= Getexactkatum(hyponym)
			if exacthyponymkatum!=None:
				exacthyponymkatum._is(exacthypernymkatum,False)

def addexceptions(filename):
    file=open(filename,"r")
    for line in file:
        word=line.split(' ')[1]
        exceptionword=line.split(' ')[0]    
        exceptionkatum = exception.Get(exception.countI + 1)
        word_katum=wordroot.Get(word)
        word_katum._is(exceptionkatum,check=False)
        exceptionkatum.Get(exceptionword)

def addantonyms(synset):
	doneantonyms[synset]=True
	exactsynset=Getexactkatum(synset)
	if exactsynset!=None:
		anotnymkatum=antonym.Get(antonym.countI)
		anotnymkatum._is(symmetrical,False)
		exactsynset._is(anotnymkatum,False)
		for anotnym_ in synset.lemmas()[0].antonyms():
			anotnymsynset=Getexactkatum(anotnym_.synset())
			if anotnymsynset!=None:
				anotnymsynset._is(anotnymkatum,False)
				doneantonyms[anotnym_.synset()]=True

katum.load('wordnetonlysynsets.datum', atum())
generalthing = datum.thing
wordnetroot=generalthing.find("wordnet")
wordroot=wordnetroot.find("wordroot")
definition=wordnetroot.find("definition")
exception = wordnetroot.Get("exception")
relation=wordnetroot.Get("relation")
symmetrical=wordnetroot.Get("symmetrical")
antonym = relation.Get("antonym")

for synset in list(wn.all_synsets()):
	name=synset.name()
	type_=name.split('.')[1]
	if(type_=='s' or type_=='a'or type_=='r'or type_=='v'or type_=='n'):
		if synset.hyponyms()!=None:
			addhyponyms(synset)
		if synset.lemmas()[0].antonyms()!=None:
			if not doneantonyms.get(synset,False):
				addantonyms(synset)

addexceptions("noun.exc")
addexceptions("adj.exc")
addexceptions("adv.exc")
addexceptions("verb.exc")
generalthing.save('wordnet-hyponyms-exceptions.datum')