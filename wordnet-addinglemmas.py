import nltk
from nltk.corpus import wordnet as wn
import re
import os
from collections import deque
os.chdir(os.getcwd())
from cpyDatumTron import atum, datum, katum, Of, Intersect, Union


def getExactSynset(syn,wordInDatum,wnr):
	wordStr=getName(syn)
	definition = wnr.find("definition")
	currentDefinition = syn.definition()
	priority=wnr.find("priority")
	word = wordStr.split('.')[0]
	pos = wordStr.split('.')[1]
	type_="notfound"	
	if (pos=='n'):
		type_="noun"
	elif(pos=='v'):
		type_="verb"
	elif(pos=='r'):
		type_="adverb"
	elif(pos=='a'):
		type_="adjective"
	if(type_!="notfound"):
		if(wordInDatum.countI>0):
			for instance in wordInDatum.I:				
				defin=definition.of(instance)
				if(defin!=None):
					if(defin.O==currentDefinition):
						return instance
	return None			

def getName(wne):
    x=wne.name()
    x=str(x)
    return x						

katum.load('wordnet-hyponyms-exceptions-topicdomains.datum', atum())
generalThing = datum.thing

wordnetRoot=generalThing.find("wordnet")
wordRoot=wordnetRoot.find("wordroot")
lemma_=wordnetRoot.get("lemma")

for word in wordRoot.I:
	wordItself=word.O	
	listOfSynsets=wn.synsets(wordItself)
	for synset in listOfSynsets:
		listOfLemmas=synset.lemma_names()
		if(len(listOfLemmas)>1):
			exactInstance=getExactSynset(synset,word,wordnetRoot)
			if(exactInstance!=None):						
				for lemma in listOfLemmas:
					if(lemma!=wordItself):					
						lemmaInstance=lemma_.get(lemma)
						exactInstance._is(lemmaInstance,False)


generalThing.save('wordnet-nohas.datum')